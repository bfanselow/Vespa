"""
 
 File: test_csv_file.py
 Description: 
  Unit-testing various operations on the CVE data stored in CSV files 
 
"""
import sys
import pytest
import datetime
import pandas as pd

sys.path.append('app')
import csvfile 
import cve_data_abstraction as cda 

CSV_FILE = "app/csv_data/cve.csv"

storage_type = 'csv'
init_args = {"file_path": CSV_FILE, 'persist': False}
   
sample_query_package = "photoshop" 
sample_query_result = [{'CVE': 'CVE-2020-0004', 'package': 'photoshop', 'vulnerable_version': '2.0.9', 'patched_version': '2.1.2'} ]
##-------------------------------------------------------------------------------------
def test_cve_csv_read():
    """ Test the csv file load by Pandas to a df """
    df = csvfile.csv_to_df(CSV_FILE)
    assert isinstance(df, pd.DataFrame) == True 

##--------------------------------------
def test_cve_dh_create():
    """ 
     Test creation of the data-access-handler for CSV file 
    """
    cve_dh = cda.create_cve_dh(storage_type, init_args) 
    assert isinstance(cve_dh, cda.CveDH) == True 

##--------------------------------------
def test_query_cve_data():
    """ 
     Test query for CVE record from CSV file
    """
    cve_dh = cda.create_cve_dh(storage_type, init_args) 
    result = cve_dh.get_cve_data_for_package(sample_query_package) 
    assert isinstance(result, list) == True 
    assert result == sample_query_result

##--------------------------------------
def test_get_timestamp():
    """ 
     Test retrieval of CSV file last-modfication timestamp (datetime object)
    """
    dt = csvfile.file_timestamp(CSV_FILE)
    assert isinstance(dt, datetime.datetime) == True 
