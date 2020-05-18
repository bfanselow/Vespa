"""

  Module: database

  Description: 
    Defines the CveRecord() model class for SqlAlchemy (table="cve_records).

    Also defines some "out-of-band" functions that are not used by the Flask service, but
    accessed manually (from venv command-line) to manage CVE data. 

    * create_tables()
      Used to create the "cve_records" table from the (venv) command-line:
      (venv) $ python -c 'import database; database.create_tables(username="vespa_admin", password="*****")'

    * csv_to_sql()
      Used to bulk load the CVE records from a CSV file into the "cve_records" table:
      (venv) $ python -c 'import database; database.csv_to_sql(csv_filepath, username="vespa_rw", password="*****")'
    
    * sql_to_csv()
      Used to create a CSV file from all CVE records in the "cve_records" table:
      (venv) $ python -c 'import database; database.sql_to_csv(csv_filepath, username="vespa_rw", password="*****")'


"""
import csv
import copy
import datetime
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.engine.url import URL
import mysql.connector

import csvfile
from config import * 


myname = os.path.basename(__file__)

PORT = 3306    
DRIVER = 'mysql+mysqlconnector'

Base = declarative_base()

##-----------------------------------------------------------------------------------------
class DatabaseError(Exception):
  pass

##-----------------------------------------------------------------------------------------
class CveRecord(Base):
    """
     Data model for CVE records
    """
    __tablename__ = 'cve_records'
    ## SQLAlchemy automatically sets AUTO_INCREMENT on the first Int primary-key col not marked as a foreign key
    id =                 Column(Integer, primary_key=True)
    ts_inserted =        Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    CVE =                Column(String(80), index=True, unique=True, nullable=False)
    package =            Column(String(128), index=True, nullable=False)
    vulnerable_version = Column(String(128), index=True, nullable=False)
    patched_version =    Column(String(128), index=True, nullable=False)

    def __init__(self, cve, package, vulnerable_version, patched_version):
        self.CVE = cve 
        self.package = package 
        self.vulnerable_version = vulnerable_version 
        self.patched_version = patched_version 

##-----------------------------------------------------------------------------------------
def create_db_engine(db_args):
  """
   Create the SqlAlchemy "engine"
   Required Arg (dict): database access parameters
   Returns (obj): SqlAlchemy database "engine"    
  """

  URI_PARAMS = {
    'drivername': DRIVER,
    'port':       PORT,
    'username':   db_args['username'],
    'password':   db_args['password'],
    'host':       db_args['host'],
    'database':   db_args['database']
  }

#  print(">>>>>>>>>>>>>>>%s" % URI_PARAMS)

  engine = create_engine(URL(**URI_PARAMS))
  
#  port = PORT
#  username = db_args['username']
#  password = db_args['password']
#  host = db_args['host']
#  database = db_args['database']
#  uri = "%s://%s:%s@%s:%d/%s" % (DRIVER, username, password, host, port, database)
#  engine = create_engine(uri)

  return(engine)

##-----------------------------------------------------------------------------------------
def process_db_args(db_default_configs, **kwargs):
  """
   Compiles a dict of database-access args (for creating engine), starting with passed 
   defaults and optionally overrideing username and/or password.
   Required arg (dict): default db-args 
   Optional kwargs: (username, password)
   Returns (dict): final db-config params
  """

  db_args = copy.deepcopy(db_default_configs)
  if 'username' in kwargs:
    db_args['username'] = kwargs['username'] 
  if 'password' in kwargs:
    db_args['password'] = kwargs['password'] 

  return( db_args )

##-----------------------------------------------------------------------------------------
def create_tables(**kwargs):
  """
   Create the "cve_records" defined by the CveRecord() model above.
   Default db-params will be read from app/config. User and password params can be overriden based on kwargs.
   Optional kwargs: (username, password)

   Typical usage:
    (venv) $ python -c 'import database; database.create_tables(username="vespa_admin", password=<ADMIN-PW>)'
  """
  tag = "%s.create_tables" % myname

  db_configs = BaseConfig.STORAGE_ARGS['database']
  db_args =  process_db_args(db_configs, **kwargs) 

  engine = create_db_engine(db_args)

  print("%s: Creating database table [%s]" % (myname, CveRecord.__table__)) 
  res = Base.metadata.create_all(bind=engine)

##-----------------------------------------------------------------------------------------
def create_session(engine):
  """
   Create the SqlAlchemy "session" object from the passed "engine".
   Required arg:
    * engine (obj): created by create_db_engine()
   Returns (obj): Database "session" object 
  """
  tag = "%s.create_session" % myname

  session = None

#  try:
#    Base.metadata.bind = engine
#    DBSession = sessionmaker(bind=engine)
#    session = DBSession()
#  except Exception as e:
#    raise

  db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

  return(db_session)
 
##-----------------------------------------------------------------------------------------
def csv_to_sql(file_path, **kwargs):
  """
   ETL function for CSV=>SQL transformation.
   Required arg (str): path to CSV file
   Optional kwargs: (username, password)
   Returns (int): Number of records inserted
 
   !!! WARNING: This will overwrite the existing CVE records in the database. No support for APPEND()
 
   Typical usage:
    (venv) $ python -c 'import database; database.sql_to_csv(csv_file, username="vespa_rw", password="*****")'
  """
  
  tag = "%s.csv_to_sql" % myname
  
  db_configs = BaseConfig.STORAGE_ARGS['database']
  db_args =  process_db_args(db_configs, **kwargs) 

  ## Load CSV file contents into Pandas df
  df = csvfile.csv_to_df(file_path)

  engine = create_db_engine(db_args)
  
  session = create_session(engine)

  tablename = CveRecord.__tablename__

  sql_truncate = 'TRUNCATE TABLE ' + tablename
  print(">> TRUNCATING TABLE: %s" % tablename)
  session.execute(sql_truncate)

  file_row_count = df.shape[0]
  for i in range(file_row_count):
    l_values = list(df.iloc[i, :])
    print(">> INSERTING: %s" % str(l_values))
    cve_rec = CveRecord(*l_values)
    session.add(cve_rec)

  session.commit()
  session.close()

  ## sanity check
  db_row_count = session.query(CveRecord.id).count()

  if file_row_count != db_row_count:
    raise DatabaseError("%s: Failed to load all (%d) records from file" % (file_row_count)) 

  return(db_row_count)

##-----------------------------------------------------------------------------------------
def sql_to_csv(file_path, **kwargs):
  """
   ETL function for SQL=>CSF transformation.
   Required arg (str): path to CSV file
   Optional kwargs: (username, password)
   Returns (int): Number of records written to file 
   
   !!! WARNING: This will overwrite the existing CVE records in the output file (if it exists).
  
   Typical usage:
    (venv) $ python -c 'import database; database.csv_to_sql(csv_file, username="vespa_rw", password="*****")'
  """
 
  tag = "%s.sql_to_csv" % myname

  ## We remove these columns/values from the database records before writing to file
  REMOVE = ['id', 'ts_inserted']
 
  db_configs = BaseConfig.STORAGE_ARGS['database']
  db_args =  process_db_args(db_configs, **kwargs) 

  engine = create_db_engine(db_args)
  session = create_session(engine)

  ## Sanity check: Perform a count() records query to validate the connection and verify data exists
  count = session.query(CveRecord.id).count()
  if not count:
    raise DatabaseError("%s: Zero CVE records stored" % (tag))
 
  tablename = CveRecord.__tablename__
  cve_records = session.query(CveRecord).all()
 
  print("%s: Writing CSV file [%s] from all records in database table [%s]" % (myname, file_path, tablename)) 

  ins = inspect(CveRecord)
  col_names = [c_attr.key for c_attr in ins.mapper.column_attrs]

  for rm in REMOVE:
    col_names.remove(rm)

  with open(file_path, 'w') as f:
    out = csv.writer(f)
    out.writerow(col_names)

    for row in session.query(CveRecord).all():
      l_row = object_to_dict(row,REMOVE).values()
      print(">> Writing row to file: %s" % str(l_row))
      out.writerow(l_row)

  print(cve_records) 

##-----------------------------------------------------------------------------------------
def object_to_dict(orm_record, remove=None):
  """ 
   Quick-n-dirty mapping of ORM row to dict.
   If passed "remove" list is populated, all keys in the list will be removed from dict
   Required Args:
    1) orm_record (obj): record form ORM query 
   Returns (dict): dict mapping of model record (with optional key removal)
  """
  d_row = { c.key: getattr(orm_record, c.key) for c in inspect(orm_record).mapper.column_attrs} 

  if remove:
    for rm in remove:
      d_row.pop(rm, None)

  return(d_row)
 
##-----------------------------------------------------------------------------------------
if __name__ == '__main__':

   
    ## input files (relative to Vespa/app dir) 
    csv_path_in = "csv_data/cve.csv"
    bad_csv_path_in = "csv_data/bogus"

    ## output files (relative to Vespa/app dir) 
    csv_path_out = "csv_data/csv_new.csv"

    username = "vespa_rw"
    password = '!Vespa_RW!'

    table_name = CveRecord.__table__

#    print("%s: Importing CSV data from file (%s) to database table (%s)..." % (myname, csv_path_in, table_name))
#    out = csv_to_sql(csv_path_in, username=username, password=password)
#    print("OUTPUT: %s" % out)

    print("%s: Exporting CVE data from database table (%s) to file (%s)..." % (myname, table_name, csv_path_out))
    out = sql_to_csv(csv_path_out, username=username, password=password)
    print("OUTPUT: %s" % out)
  
