"""
 Module: config.py
 Description:
   BaseConfig() class (and child classes) for VESPA Flask application configuration 
   for multiple environments.  Default configs are set in BaseConfig() attributes. 
   Child classes of BaseConfig() used for each specific environment. 

 Avaialable config classes:
  * BaseConfig(object):
  * ProductionConfig(BaseConfig):
  * DevelopmentConfig(BaseConfig):
  * TestingConfig(BaseConfig):


"""
import os

##====================================================================================
class BaseConfig(object):
  """
  Base (Default) Application Configuration settings
  """ 

  DEBUG = False 
  TESTING = True
  VERSION = 2.0

  APP_CONTACT = 'bfanselow@gmail.com'

  ##==================================
  ## Api Key
  ## Using an API-key like this for GET or POST requests is not intended to be a 
  ## strong Security measure, but rather a placeholder for future implementation 
  ## of a more secure API-authorization scheme. 
  ##==================================
  API_KEY = 'William.Fanselow.Vespa.2.0'

  ##==================================
  ## App paths
  ##==================================
  ## Directory containing this file
  ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

  ## Logfile directory and path (NOT USED)
  LOG_DIR = os.path.join(ROOT_DIR, 'logs') 
  LOGFILE_PATH = LOG_DIR + '/vespa.log'

  CVE_DATAFILE_PATH =  os.path.join(ROOT_DIR, 'csv_data/cve.csv')

  ##==================================
  ## CVE-data Storage type. 
  ## See cve_data_abstraction.py for all supported types
  ##==================================
  STORAGE_TYPE = 'csv'
  STORAGE_ARGS = {
    'csv': {
       'file_path': CVE_DATAFILE_PATH, 
       'persist': True  ## if persist=True: load on init and on on every query
                        ## if persist=False: reload on every query
    },
    'database': {
      'host': "127.0.0.1",
      'port': 3306,
      'database': 'vespa',
      'username': 'vespa_ro',
      'password': '!Vespa_RO!' 
    }
  }

##====================================================================================
##====================================================================================
class ProductionConfig(BaseConfig):
  """
  Production Environment Configurations
  """ 
  DEBUG = False
  TESTING = False

##====================================================================================
class DevelopmentConfig(BaseConfig):
  """
  Development Environment Configurations
  """ 
  DEBUG = False 
  TESTING = False

##====================================================================================
class TestingConfig(BaseConfig):
  """
  Testing Environment Configurations
  """ 
  DEBUG = False 
  TESTING = True

