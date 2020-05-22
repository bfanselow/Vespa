"""

  Module: cve_data_abstraction.py
  Description:
   Provides a CVE data storage-abstraction-layer object for accessing CVE data in 
   different storage formats.
  
   Storage-type is configured in Flask app/config.py

   CveDH_<storage-type>() objects are not intended to be instanitated directly. Use 
   the create_cve_dh(storage_type) function instead which will return a CveDH_<type> object.  
   Use this object to query CVE data for records associated with a specific package.
     cve_dh = create_cve_dh(storage_type)
     ...
     d_pgk_data = CveDH_<type>.get_cve_data_for_package(package_name)

   Using a storage-absraction-layer gives us the flexibility to store CVE data in
   different storage formats (CSV-file, YAML, database, remote-API, etc.) and access
   this data with a single common access methods independent of the format. 
   It also gives flexibility on how we load and query the data.  For example, if the
   CVE data is stored in a local csv file, there are a couple of options for how we 
    read/query the data.
     1) Load the entire CSV file upon app-initialization, and access the in-memory data 
        store for CVE queries.
        * Advantage: better app/api performance without file-handling on each query. 
        * Disadvantage: creates possibility of querying "stale" CVE data 
          (though we do have a "refresh" capability from the API)
     2) Load the data from file upon each CVE query. 
        * Advantage: less chance of querying "stale" CVE data. 
        * Disadvantage: decreased performance with all the file-handling. 

"""

import logging
import os 
import sys
import abc
import time
from sqlalchemy import func
from sqlalchemy.orm import class_mapper

## database model handling 
import database

## csv-file handling 
import csvfile

STORAGE_TYPES = ['csv', 'database']  
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

DEBUG = 2 

myname = os.path.basename(__file__)

##----------------------------------------------------------------------------------------------
def create_cve_dh(storage_type, d_args):
  """
   Top-level enty point for creating a CveDH object for a specific storage type.
   Required args: (2 positional)
    1) storage_type (str): - one of the supported storage type identifiers
    2) d_args (dict): - initialization args for the CveDH() object
  Raises: CveStorageError() if unsupported storage type or unable to init CveDH() object 
  Returns:  CveDH_<storage_type>() object which servers as a CVE-datahandler from which to query data.
  """
  tag = "%s.create_cve_dh" % myname

  cve_dh = None

  if storage_type not in STORAGE_TYPES:
    raise CveStorageError("%s: Unsupported storage type: [%s]" % (tag, storage_type))

  ## TODO: refactor this using Class-factory logic 
  if storage_type == 'csv':
    dh_class = CveDH_CSV
  elif storage_type == 'database':
    dh_class = CveDH_Database
  elif storage_type == 'api':
    dh_class = CveDH_Api

  d_args['storage_type'] = storage_type

  ## instantiate
  cve_dh = dh_class(d_args)
   
  return cve_dh

##----------------------------------------------------------------------------------------------
class CveStorageError(Exception):
    pass

##----------------------------------------------------------------------------------------------
class InitError(Exception):
    pass

##----------------------------------------------------------------------------------------------
class CveDH(abc.ABC):
  """ 
   Abstract-Base-Class for the CVE data-hander.  As an abstract class this Class cannot be 
   instantiated. Its purpose is to enforce the implementation behavior of its (child) sub-classes.
   All subclasses must implement methods decorated with @abc.abstractmethod 
      * initialize_storage(d_args=None)
      * refresh_storage()
      * get_cve_data_for_package(package_name)
      * resource_cleanup()
  """ 
  
  ##---------------------------------------------------- 
  def __init__(self, d_init_args):
    self.cname = self.__class__.__name__
    self.DEBUG = DEBUG
    
    self.storage_type = d_init_args.get('storage_type', None)
    if not self.storage_type:
      raise InitError("%s: Missing required init() parameter: [storage_type]" % (self.cname))
    
    self.logger = None 
    if 'logger' in d_init_args: 
      self.logger = d_init_args['logger']

  ##---------------------------------------------------- 
  def log(self, s_level, msg ):
    """
     Internal logging functionality. Uses logger if defined, otherwise STDOUT
    """
    if self.logger is None:
      print("%s: %s" % (s_level, msg))
    else:
      numeric_level = getattr(logging, s_level.upper(), None)
      if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % loglevel)
      self.logger.log(numeric_level, msg)

  ##---------------------------------------------------- 
  @abc.abstractmethod
  def initialize_storage(self, d_args=None):
    pass ## implemented entirely by child function

  ##---------------------------------------------------- 
  @abc.abstractmethod
  def refresh_storage(self):
    pass ## implemented entirely by child function

  ##---------------------------------------------------- 
  @abc.abstractmethod
  def resource_cleanup(self):
    pass ## implemented entirely by child function

  ##---------------------------------------------------- 
  @abc.abstractmethod
  def data_timestamp(self):
    pass ## implemented entirely by child function

  ##---------------------------------------------------- 
  @abc.abstractmethod
  def get_cve_data_for_package(self, package_name):
    pass ## implemented entirely by child function

##----------------------------------------------------------------------------------------------
## CveDH_CSV
##----------------------------------------------------------------------------------------------
class CveDH_CSV(CveDH):
  """ 
   CVE data-handler for CSV file storage.
   CVE-data is made accessible as an attribute (data) of the instantiated class, in the form of
   a Pandas dataframe. Queries are made directly to this Pandas df object.
  """ 
  def __init__(self, d_init_args):

    ## Call parent __init__()
    super().__init__(d_init_args) 

    self.cname = self.__class__.__name__
    
    self.data = None ## this is our Pandas df loaded from CVE file

    ## Init once and keep in app context or re-init on each query
    self.persist = d_init_args.get('persist', True) 

    file_path = d_init_args.get('file_path', None)
    if not file_path:
      raise InitError("%s: Missing required init() parameter: [file_path]" % (self.cname))
    self.file_path = file_path

    if self.persist: ## load the data into app-context memory now and not have to do it on every query
      status = self.initialize_storage(d_init_args)

  ##---------------------------------------------------- 
  def initialize_storage(self, d_args=None):
    """
     Load data from CSV file into an object-storage attribute.
     We assume that the CSV files has comma-sep column names in the first line.
     Returns (bool):  True|False for status of operation 
    """ 
    tag = "%s.initialize_storage" % (self.cname) 

    status = False

    file_path = self.file_path
    self.log('DEBUG', "%s: Reading data file into memory: %s" % (tag, file_path))
  
    if DEBUG: 
      ts_1 = time.perf_counter()
    try:
      self.data = csvfile.csv_to_df(file_path)
      status = True
    except Exception as e:
      raise

    if DEBUG: 
      ts_2 = time.perf_counter()
      ts_elapsed = ts_2 - ts_1
      self.log('INFO', "%s: Data-file read elapsed time (secs): %s" % (tag, round(ts_elapsed,2)))

    return status

  ##---------------------------------------------------- 
  def refresh_storage(self):
    """
     Drop self.data and reload data from CSV file into self.data.
     Returns (bool):  True|False for status of operation 
    """ 
    tag = "%s.refresh_storage" % (self.cname) 
    self.data = None
    status = False
    self.log("INFO", "%s: Refreshing in-memory cve-data..." % (tag))
    try: 
      status = self.initialize_storage()
    except Exception as e:
      self.log('ERROR', "%s: self.initialize_storage() failed with exception: %s" % (tag, e))
      raise
    return status

  ##---------------------------------------------------- 
  def data_timestamp(self):
    """
     Get the file-modification attribute as the last update timestamp 
     Returns (str): timestamp
    """ 
    tag = "%s.data_timestamp" % (self.cname) 
  
 
    try: 
      dt_last_mod = csvfile.file_timestamp(self.file_path) 
    except Exception as e:
      self.log('ERROR', "%s: csvfile.file_timestamp(() failed with exception: %s" % (tag, e))
      raise
      
    ts_last_mod = dt_last_mod.strftime(TIMESTAMP_FORMAT)

    return ts_last_mod

  ##---------------------------------------------------- 
  def get_cve_data_for_package(self, package_name):
    """
     Query Panads dataframe of CVE data for specific package.
     Required arg (str): package name
     Returns (list): List of dicts - CVE data rows have matching package-name. Could be empty list 
    """ 
    tag = "%s.query_data" % (self.cname) 
    if self.data is None:
      self.log("WARNING", "%s: In-memory cve-data no longer exists. Reloading..." % (tag))
      try: 
        status = self.initialize_storage()
      except Exception as e:
        self.log('ERROR', "%s: self.initialize_storage() failed with exception: %s" % (tag, e))
        raise

    df = self.data

    self.log("DEBUG", "%s: Querying CVE data in CSV-file for package=[%s]..." % (tag, package_name))
    ## Use Panda's efficient row query
    df_package_data = df.loc[df['package'] == package_name]

    ## convert to list of dicts
    l_package_data = df_package_data.to_dict('records')

    if not self.persist:  ## Drop the in-mem data
      self.data = None

    return l_package_data

  ##---------------------------------------------------- 
  def resource_cleanup(self):
    """
     Called on __exit__, will properly close any file resources .
     Nothing to do as Pandas took care of proper file closing, etc.
    """ 
    tag = "%s.resource_cleanup" % (self.cname) 
    self.log('INFO', "%s: Cleaning up..." % (tag))


##----------------------------------------------------------------------------------------------
## CveDH_Database
##----------------------------------------------------------------------------------------------
class CveDH_Database(CveDH):
  """ 
   CVE data handler for database storage. Currently using Flask-SqlAlchemy ORM for access 
   to mariaDB. 
   CVE-data is made accessible as an SQLAlchemy "session" object stored as an attribute of the
   instantiated class.
  """ 
  ##---------------------------------------------------- 
  def __init__(self, d_init_args):
    ## Call parent __init__()
    super().__init__(d_init_args) 
    self.cname = self.__class__.__name__

    self.session = None ## this provides access to the data
 
    ## Verify we have all required DB params
    if 'host' not in d_init_args:  
      raise InitError("%s: Missing required init() parameter: [host]" % (self.cname))
    if 'database' not in d_init_args:  
      raise InitError("%s: Missing required init() parameter: [database]" % (self.cname))
    if 'username' not in d_init_args:  
      raise InitError("%s: Missing required init() parameter: [username]" % (self.cname))
    if 'password' not in d_init_args:  
      raise InitError("%s: Missing required init() parameter: [password]" % (self.cname))
    
    self.db_args = {
      'host': d_init_args['host'],
      'database': d_init_args['database'],
      'username': d_init_args['username'],
      'password': d_init_args['password']
    }   

    self.initialize_storage(self.db_args)

  ##---------------------------------------------------- 
  def initialize_storage(self, db_args):
    """
     Initializes DB tables and sets up connection.
     Creates a SQLAlchemy "session" object to be used for queries. 
     Returns (bool):  True|False for status of operation 
    """ 
    tag = "%s.initialize_storage" % (self.cname) 

    status = False
    port = db_args.get('port', database.PORT)

    self.log("DEBUG", "%s: Connecting to database..." % (tag))
    engine = database.create_db_engine(db_args)
 
    ## store the db-engine as object-attr for full resource_cleanup()
    self.db = engine

    ## Create database session and store as object-attr
    self.log("DEBUG", "%s: Creating DB session..." % (tag))
    try:
      self.session = database.create_session(engine)
      status = True 
    except Exception as e:
      raise
 
    self.session.close()
    ## Perform a count() records query to validate the connection and verify data exists
    count = self.session.query(database.CveRecord.id).count() 
    if not count:
      raise CveStorageError("%s: Zero CVE records stored" % (tag))
    
    self.log("INFO", "%s: CVE records in database: (%d)" % (tag, count))

    return status

  ##---------------------------------------------------- 
  def refresh_storage(self):
    """
     Drop database connections and re-establish.
     Returns (bool):  True|False for status of operation 
    """ 
    tag = "%s.refresh_storage" % (self.cname) 
    status = False
    self.log("INFO", "%s: Refreshing database resources..." % (tag))

    ## First we close all DB resources
    self.resource_cleanup()

    ## Now re-connect, etc.
    try:
      self.initialize_storage(self.db_args)
      status = True
    except Exception as e:
      self.log("ERROR", "%s: initialize_storage() failed with exception: %s" % (tag,e))
      raise

    return status

  ##---------------------------------------------------- 
  def data_timestamp(self):
    """
     Get the max(ts_inserted) from the "cve_records" table 
     Returns (str): max(ts_inserted)
    """ 
    tag = "%s.data_timestamp" % (self.cname) 

    ## tuple
    cve_record = self.session.query(func.max(database.CveRecord.ts_inserted)).first()
    self.session.close()
    dt_last_insert = cve_record[0]
    ts_last_insert = dt_last_insert.strftime(TIMESTAMP_FORMAT)

    return ts_last_insert

  ##---------------------------------------------------- 
  def resource_cleanup(self):
    """
     Cleanup up all database resources 
    """ 
    tag = "%s.resouce_cleanup" % (self.cname) 
    self.log("DEBUG", "%s: Cleaning up database resources..." % (tag))
    if self.session is not None:
      self.session.remove()
    self.db.dispose()

  ##---------------------------------------------------- 
  def get_cve_data_for_package(self, package_name):
    """
     Query Database table of CVE data for specific package.
     Required arg (str): package name
     Returns (list): List of dicts - CVE data rows have matching package-name. Could be empty list 
    """ 
    tag = "%s.get_cve_data_for_package" % (self.cname) 
    self.log("DEBUG", "%s: Querying CVE database for package=[%s]..." % (tag, package_name))

    ## Use custom @classmethod query defined in model to retrieve matching records
    result = database.CveRecord.records_for_package(self.session, package_name) 

    self.session.close()

    ## rec_formatter() gives us a dict representation of specific cols in record
    cve_records = [record.rec_formatter() for record in result]

    return cve_records

 
##----------------------------------------------------------------------------------------------
## Placeholder for other formats 
##----------------------------------------------------------------------------------------------
#class CveDH_Yaml(CveDH):
#  pass
#class CveDH_API(CveDH):
#  pass
##----------------------------------------------------------------------------------------------

if __name__ == '__main__':
 
  ## Test CSV by default
  storage_type = 'csv'
  file_path = 'csv_data/cve.csv'
#  file_path = 'csv_data/bad_cve_data.1.csv'
#  file_path = 'csv_data/bad_cve_data.2.csv'
#  file_path = 'csv_data/bad_cve_data.3.csv'
  d_args = {'file_path': file_path}

  ## Test database
  if len(sys.argv) > 1:
    if sys.argv[1] == 'database':
      from config import DevelopmentConfig
      storage_type = 'database'
      d_args = DevelopmentConfig.STORAGE_ARGS[storage_type]
 
  print("Creating CVE-access--handler for storage-type: [%s]" % (storage_type))
  cve_dh = create_cve_dh(storage_type, d_args) 
  print(" Data-access-handler is ready for access")
