#!/usr/bin/env python
"""
  File: version_math.py

  Description:
   Perform comparative analysis of version strings.
   Primary function: is_version_in_window()

  Requiers: pip install packaging
    (Implements PEP 0440 version identification)

"""

from packaging.version import parse as parse_version
import os
import re

myname = os.path.basename(__file__)

##--------------------------------------------------------------------------------------------
class VersionError(Exception):
   pass

##--------------------------------------------------------------------------------------------
def is_version_in_window(version, version_lo, version_hi):
    """
     Descr:
       Compare a version string to to a pair of low and high version strings
       to identify if the version string is "inside" the window between the low
       and high versions.
       !!! In this case "inside the version window" is defined by:
       !!!   "greater than or equal to the low version AND less than the high version" 
     Required args (3 positional):
      1) version (str): the version string to be checked
      2) version_lo (str): the version str identifying the low end of the window 
      3) version_hi (str): the version str identifying the high end of the window 
     Raises: VersionError() if the input version strings do not pass some sanity checks.
     Returns (bool):
      * True  - if input version is "inside" of the version window (version_lo <= version < version_hi) 
      * False - if input version is NOT "inside" the version window (version < version_lo and version >= version_hi) 
    """

    ## Sanity checks:
    ## 1) all version strings must start with int and contain only int and "."
    v = version
    for v in (version, version_lo, version_hi): 
      if not re.match(r'^\d+', v):
        raise VersionError("%s: Unsupported version format (%s). Must start with digit" % (myname, v)) 
      if not re.match(r'^[0-9.]+$', v):
        raise VersionError("%s: Unsupported version format (%s). Must contain only digits and dots" % (myname, v)) 
      if '..' in v:
        raise VersionError("%s: Unsupported version format (%s). Must contain only single dot between digits" % (myname, v)) 
 
    ## 2) version_lo must be LESS than version_hi
    if parse_version(version_lo) >= parse_version(version_hi):
      raise VersionError("%s: Invalid input versions - version_lo (%s) must be leass than version_hi (%s)" % (myname, version_lo,version_hi)) 

    if parse_version(version) < parse_version(version_lo):    ## is version <= version_lo? - NOT in window 
        return False
    elif parse_version(version) >= parse_version(version_hi): ## is version >= version_hi? - NOT in window 
        return False
    else: ## we must be in window
        return True

##--------------------------------------------------------------------------------------------
if __name__ == '__main__':

  ## simple test/demo of method. Not to take place of pytest unit-tests!

   input_version_tups = [ 
    ("1.2.1", "1.2.1", "1.2.1"),  # v_lo == v_hi
    ("1.2.1", "1.2.2", "1.2.3"),  # True
    ("1.2.1", "1.2.0", "1.2.4"),  # False
    # sanity check: try some alphas or other unsupported chars in verison string 
    ("0,0.10", "0.0.1", "0.1.1"),       
    ("0..0.10", "0.0.1", "0.1.1"),       
    ("v0.0.10", "0.0.1", "0.1.1"),       
    ("v0.0.10", "0.0.1a6", "0.1.1-beta")
   ]

   for version_inputs in input_version_tups:
     try:
       result = is_version_in_window( *version_inputs )
       print("%s: RESULT=%s - (v, v_lo, v_hi)=%s" % (myname, result, version_inputs)) 
     except Exception as e:
       print("%s: ERROR - is_version_in_window() failed with exception: %s" % (myname, e)) 
 

