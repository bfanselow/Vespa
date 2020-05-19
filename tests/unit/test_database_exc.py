"""
 
 File: test_database.py
 Description: 
  Unit-testing various operations on the CVE data stored in database 
 
"""
import sys
import pytest

sys.path.append('app')
import database 
from database import DatabaseError

import cve_data_abstraction as cda
from cve_data_abstraction import CveDH_Database, InitError

from config import BaseConfig
storage_type = 'database'
db_args = BaseConfig.STORAGE_ARGS[storage_type]

storage_type = 'database'
invalid_init_args = {"username": "vespa"}

##-------------------------------------------------------------------------------------
def test_create_engine_exc():
    """ Test proper exception handling of SQL-Alchemy engine creation (bad input args) """
    with pytest.raises(DatabaseError):
      engine = database.create_db_engine(invalid_init_args)

##---------------------------------
def test_csv_dh_init_exc():
    """
     Verify that CveDH_Database.init() raise an InitError() exception as expected with invalid init parameters
    """
    with pytest.raises(InitError):
        cve_dh = cda.CveDH_Database(invalid_init_args)
