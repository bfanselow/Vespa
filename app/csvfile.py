"""

  Module: csvfile 

  Description: 
    Functions for handling CSV files and their CVE data 

"""
import os
import pathlib
import datetime
import pandas as pd
from pathlib import Path

myname = os.path.basename(__file__)

## Required CSV column names
COLUMNS = ['CVE', 'package', 'vulnerable_version', 'patched_version'] 

##-----------------------------------------------------------------------------------------
class CsvFileError(Exception):
  pass

##-----------------------------------------------------------------------------------------
def csv_to_df(file_path):
  """
   Read the csv file and load it into Pandas dataframe.  We do NOT assume the data is "clean".
   Required arg:
     * file_path (str): path to local file
   Raises: CsvFileError() if file read errors, or formatting errors
   Returns: pd dataframe of cve data
  """

  tag = "%s.csv_to_df" % myname 
  d_cve_data = None

  if not Path(file_path).is_file():
    raise CsvFileError("%s: CSV-file not found: [%s]" % (tag, file_path))

  try:
    df = pd.read_csv(file_path, usecols=COLUMNS)
  except Exception as e:
    raise CsvFileError("%s: CSV-file format error: [%s]" % (tag, e))
  for col in COLUMNS:
    if any(df[col].isnull()):
      raise CsvFileError("%s: Missing required column: [%s]" % (tag, col))

  return df
 
##-----------------------------------------------------------------------------------------
def file_timestamp(file_path):
  """
   Get the file-modification attribute as the last update timestamp
   Required arg:
     * file_path (str): path to local file
   Raises: CsvFileError() if file read errors
   Returns (obj): datetime-object 
  """
  tag = "%s.file_timestamp" % myname 

  if not Path(file_path).is_file():
    raise CsvFileError("%s: CSV-file not found: [%s]" % (tag, file_path))

  path = pathlib.Path(file_path)
  last_modified = path.stat().st_mtime
  dt_last_mod = datetime.datetime.fromtimestamp(last_modified)

  return dt_last_mod
 
##-----------------------------------------------------------------------------------------
if __name__ == '__main__':

    ## File paths relative to Vespa/app dir
    csv_file = "csv_data/cve.csv"
    csv_file_bogus = "csv_data/bougs"

    df = csv_to_df(csv_file) 
    print("CVE Pandas:\n%s\n" % df)

    ts_last_mod = file_timestamp(csv_file) 
 
    dtype = type(ts_last_mod)
    print("Type: %s" % dtype)
    print("Timestamp: %s" % ts_last_mod)
