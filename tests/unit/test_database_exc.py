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

CSV_FILE = "app/csv_data/cve.csv"

##-------------------------------------------------------------------------------------
def test_create_engine():
    """ 
    """
    df = csvfile.csv_to_df(CSV_FILE)
    assert isinstance(df, pd.DataFrame) == True 

def test_create_session():
    """ 

    """
    storage_type = 'csv'
    init_args = {"file_path": CSV_FILE, 'persist': False}
    cve_dh = cda.create_cve_dh(storage_type, init_args) 
    assert isinstance(cve_dh, cda.CveDH) == True 

def test_query_cve_data():
    """ 

    """
    storage_type = 'csv'
    init_args = {"file_path": CSV_FILE, 'persist': False}
    cve_dh = cda.create_cve_dh(storage_type, init_args) 
    assert isinstance(cve_dh, cda.CveDH) == True 

def test_query_timestamp():
    """ 

    """
    storage_type = 'csv'
    init_args = {"file_path": CSV_FILE, 'persist': False}
    cve_dh = cda.create_cve_dh(storage_type, init_args) 
    assert isinstance(cve_dh, cda.CveDH) == True 

