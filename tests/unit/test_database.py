"""
 
 File: test_database.py
 Description: 
  Unit-testing various operations on the CVE data stored in database
 
"""
import sys
import pytest
import pandas as pd
import sqlalchemy

sys.path.append('app')
import database 
import cve_data_abstraction as cda 

from config import BaseConfig
storage_type = 'database'
db_args = BaseConfig.STORAGE_ARGS[storage_type]

sample_query_package = "photoshop"
sample_query_result = [{'CVE': 'CVE-2020-0004', 'package': 'photoshop', 'vulnerable_version': '2.0.9', 'patched_version': '2.1.2'} ]

##-------------------------------------------------------------------------------------
def test_create_engine():
    """ Test SQL-Alchemy engine creation """
    engine = database.create_db_engine(db_args) 
    assert isinstance(engine, sqlalchemy.engine.base.Engine) == True 

##-----------------------------------
def test_create_session():
    """ Test SQL-Alchemy session creation """
    engine = database.create_db_engine(db_args) 
    session = database.create_session(engine) 
    assert isinstance(session, sqlalchemy.orm.scoping.scoped_session) == True 

##-----------------------------------
def test_cve_dh_create():
    """ 
     Test creation of the data-access-handler for CVE database 
    """
    init_args = db_args 
    cve_dh = cda.create_cve_dh(storage_type, init_args) 
    assert isinstance(cve_dh, cda.CveDH) == True 

##--------------------------------------
def test_query_cve_data():
    """
     Test query for CVE record from CSV file
    """
    cve_dh = cda.create_cve_dh(storage_type, db_args)
    result = cve_dh.get_cve_data_for_package(sample_query_package)
    assert isinstance(result, list) == True
    assert result == sample_query_result


