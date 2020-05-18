"""
 
 File: test_csv_file.py
 Description: 
  Unit-testing various operations on the CVE data stored in CSV files 
 
"""
import sys
import pytest
import pandas as pd

sys.path.append('app')
import csvfile 
import cve_data_abstraction as cda 

CSV_FILE = "app/csv_data/cve.csv"

##-------------------------------------------------------------------------------------
def test_cve_csv_read():
    """ Test the csv file load by Pandas to a df """
    df = csvfile.csv_to_df(CSV_FILE)
    assert isinstance(df, pd.DataFrame) == True 

def test_cve_dh_create():
    """ 
     Test creation of the data-access-handler for CSV file 
    """
    storage_type = 'csv'
    init_args = {"file_path": CSV_FILE, 'persist': False}
    cve_dh = cda.create_cve_dh(storage_type, init_args) 
    assert isinstance(cve_dh, cda.CveDH) == True 


