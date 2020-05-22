#!/usr/bin/env python
"""
  Module: cve_analysis.py
  Description:
   Functions for performing vulnerability analysis of a "package-version-host" list.
   Uses "version_math.py" to check version vulnerability. 

  Requiers: pip install packaging (Implements PEP 0440 version identification)

"""
import sys
import os
import re

import version_math

myname = os.path.basename(__file__)

##--------------------------------------------------------------------------------------------
def analyze_vulnerable_package_list(l_pvh_data, cve_dh): 
  """
   Descr:
    Take a list of "package-version-host" objects, and assess the vulnerability of the 
    of each package/version based on stored CVE records for the given host. 
   Required args (2 positional):
     1) l_pvh_data (list): list of "package-version-host" objects 
     2) cve_dh (obj): this is a DAL "data-handler" object for CVE data. Used to access CVE data stores. 
   Returns (dict): Result of vulnerability analysis. Format: <host> => [list of all vulnerable CVE-ids] 
                   Example: {"<host>": [<cve_id1>,...<cve_idN>]} or {} if no vulnerable packages for this host.

   !!! Input data is assumed to have been sanitized/validated already. For the VESPA app,
       the API has already validated the input, so we do not re-validate it here.
  """

  d_results = {}

  ## iterate over "package-version-host" object list
  for pvh in l_pvh_data:
    package_name = pvh.get('package', None)
    version = pvh.get('version', None)
    host = pvh.get('host', None)

    ## get all CVE data rows for this package by querying CVE data-handler
    try:
      l_cve = cve_dh.get_cve_data_for_package(package_name)
    except Exception as e:
      raise

    for d_row in l_cve:
      cve_id = d_row['CVE']
      vulnerable_version = d_row['vulnerable_version']
      patched_version = d_row['patched_version']

      ## check if package/version is vulnerable
      is_affected = True  ## "fail safe" 
      try:
        is_affected = is_vulnerable_version(version, vulnerable_version, patched_version)
      except Exception as e:
        raise

      ## append to list if affected
      if is_affected:
        if host not in d_results:
          d_results[host] = [] 
        d_results[host].append( cve_id ) 

  return d_results

##--------------------------------------------------------------------------------------------
def is_vulnerable_version(version, version_first_affected, version_first_patched):
  """
    Using version_math.py identify if the passed version is inside the affected version window
    and therefore affected by the vulnerability
    Required args: (3 positional)
     1) version (str): Package version to be checked. 
     2) version_first_affected (str): First affected version of package based on CVE data 
     3) version_first_patched (str): First patched version of package based on CVE data 
   Returns (bool):
    * True  - if input version is "inside" of the vulnerable versions window (v_first_aff <= version < v_first_patch)
    * False  - if input version is NOT "inside" of the vulnerable versions window (version < v_first_aff AND version >= v_first_patch)

  """
  is_in_window = True 
  try:
    is_in_window = version_math.is_version_in_window(version, version_first_affected, version_first_patched)
  except Exception as e:
    raise

  return is_in_window

##--------------------------------------------------------------------------------------------
if __name__ == '__main__':

  import cve_data_abstraction

  ## simple test/demo of method. Not to take place of pytest unit-tests!

  l_payloads = [
    [{"package": "freeciv", "version": "1.7.0", "host": "2b09375594f9499698a39749ec773c3f.example.org"}, {"package": "mint-linux", "version": "2012.6.0", "host": "2b09375594f9499698a39749ec773c3f.example.org"}, {"package": "osquery", "version": "2.7.5", "host": "2b09375594f9499698a39749ec773c3f.example.org"}],
    [{"package": "freeciv", "version": "1.1.2", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, {"package": "photoshop", "version": "2.1.1", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, {"package": "freeciv", "version": "1.0.9", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, {"package": "flash", "version": "78.3.9", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, {"package": "mint-linux", "version": "2015.2.0", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}],
  ]

  ## Test CSV by default  
  storage_type = 'csv'
  file_path = 'csv_data/bad_cve_data.3.csv'
  file_path = 'csv_data/cve.csv'
  d_args = {'file_path': file_path}

  ## Test database
  if len(sys.argv) > 1:
    if sys.argv[1] == 'database':
      from config import BaseConfig
      storage_type = 'database'
      d_args = BaseConfig.STORAGE_ARGS[storage_type]

  ## Create our CVE data-handler
  print("Creating CVE data-handler for storage-type: [%s]" % (storage_type))
  cve_dh = cve_data_abstraction.create_cve_dh(storage_type, d_args)

  for input_payload in l_payloads:
    print("%s: INPUT: %s" % (myname, str(input_payload)))
    try:
      d_result = analyze_vulnerable_package_list(input_payload, cve_dh)
      print("%s: RESULT: %s\n" % (myname, str(d_result))) 
    except Exception as e:
      print("%s: ERROR - analyze_vulnerable_package_list() failed with exception: %s" % (myname, e)) 
