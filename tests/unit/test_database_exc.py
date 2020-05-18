"""
 
 File: test_database.py
 Description: 
  Unit-testing various operations on the CVE data stored in database 
 
"""
import sys
import pytest

sys.path.append('app')
import database 
import cve_data_abstraction as cda 

from config import BaseConfig
storage_type = 'database'
db_args = BaseConfig.STORAGE_ARGS[storage_type]

##-------------------------------------------------------------------------------------
#def test_create_engine_exc():
#    """ 
#     Test creation of the SqlAlchemy "engine"
#    """

##---------------------------------
#def test_create_session_exc():
#    """ 
#
#    """
#    storage_type = 'csv'
#    init_args = {"file_path": CSV_FILE, 'persist': False}
#    cve_dh = cda.create_cve_dh(storage_type, init_args) 
#    assert isinstance(cve_dh, cda.CveDH) == True 

##---------------------------------
def test_csv_dh_init_exc():
    """
     Verify that CveDH_CSV.init() raise an InitError() exception as expected with invalid init parameters
    """
    with pytest.raises(InitError):
        cve_dh = cda.CveDH_CSV(invalid_init_args)

##---------------------------------
def test_cve_dh_create_exc():
    """
     Verify that cda.create_cve_dh() raise an CveStorageError() exception as expected with invalid storage-type
    """
    with pytest.raises(CveStorageError):
        cve_dh = cda.create_cve_dh(invalid_storage_type, {})

