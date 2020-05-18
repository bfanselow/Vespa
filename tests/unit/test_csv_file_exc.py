"""
 
 File: test_csv_file_exc.py 
 Description: 
  Verify all expected exceptions are raised by csvfile handling in modules:
    * csvfile
    * cve_data_abstraction 
 
"""
import sys
import pytest
import pandas as pd

sys.path.append('app')
import csvfile 
from csvfile import CsvFileError

import cve_data_abstraction as cda
from cve_data_abstraction import CveDH_CSV, InitError, CveStorageError

CSV_FILE = "app/csv_data/cve.csv"
BAD_CSV_PATH = "app/data/cve.csv"

## invalid file formats
INVALID_CSV_FILES = [
  "app/csv_data/bad_cve_data.1.csv", 
  "app/csv_data/bad_cve_data.2.csv", 
  "app/csv_data/bad_cve_data.3.csv"
]

storage_type = 'csv'
init_args = {"file_path": CSV_FILE, 'persist': False}

invalid_storage_type = 'textfile'
invalid_init_args = {'persist': False}

##-------------------------------------------------------------------------------------
def test_csv_file_load_exc():
    """
     Verify that csvfile.csv_to_df() raise a CsvFileError() exception as expected with non-existent file path 
    """
    with pytest.raises(CsvFileError):
        df = csvfile.csv_to_df(BAD_CSV_PATH)

##---------------------------------
@pytest.mark.parametrize("invalid_cve_file", INVALID_CSV_FILES)
def test_csv_invalid_file_format_exc(invalid_cve_file):
    """
     Verify that csvfile.csv_to_df() raise a CsvFileeError() exception as expected with 3 invalid file formats 
    """
    with pytest.raises(CsvFileError):
        df = csvfile.csv_to_df(invalid_cve_file)

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

