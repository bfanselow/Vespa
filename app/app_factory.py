"""

  File: app_factory.py
  Description: Flask application "factory" for the VESPA service.
  Last update: 2020-05-14  Bill Fanselow

"""
import sys
import os
import atexit
import logging

from flask import Flask, request, g
from config import *

import cve_data_abstraction
import CustomLogging

from blueprints.api.routes import bp_api
## Future versions UI: from blueprints.ui.routes import bp_ui


DEBUG = 0

##---------------------------------------------------------------------------------------
def create_app(d_init):
  """
   Create Flask instance (app context).
   Return app object
  """
  
  app = Flask(__name__)

  ## ignore trailing slashes in a URL ("../myMethod/" is treated same as "/myMethod")
  app.url_map.strict_slashes = False

  ## load app configurations 
  ConfigClass = d_init.get('config_class', DevelopmentConfig)
  _load_configs(app, ConfigClass)

  ## set-up logging
  _setup_logging(app) 

  with app.app_context():
    atexit.register(_cleanup, app)

    ## initialize CVE-data storage
    _init_data_storage(app) 

    _register_blueprints(app)

    return( app )

##---------------------------------------------------------------------------------------
def _init_data_storage(app):
  """
   Initialize CVE data-storage handler using CveDal() data-abstraction layer class.
  """

  print("Initializing CVE data Storage ...")

  storage_type = app.config['STORAGE_TYPE']
  storage_args = app.config['STORAGE_ARGS']
  
  app.logger.info("Initializing storage for type (%s)" % (storage_type))

  d_args = storage_args[storage_type]
  d_args['logger'] = app.logger

  cve_dh = cve_data_abstraction.create_cve_dh(storage_type, d_args)

  app.cve_dh = cve_dh
 
##---------------------------------------------------------------------------------------
def _load_configs(app, ConfigClass):
  """Load app configuration settings"""
  print("Loading configs...")
  app.config.from_object(ConfigClass)
  if DEBUG > 2:
    app.debug = True 

##---------------------------------------------------------------------------------------
def _setup_logging(app):
  """Initialize app logging"""

  print("Initializing logging...")
  min_level = logging.DEBUG
  logfile_path = app.config['LOGFILE_PATH']
  formatter = logging.Formatter('%(asctime)s  %(source_ip)15s  %(levelname)-8s %(message)s', '%Y-%m-%d %H:%M:%S')

  app.logger.handlers = [] ## we have to remove the default Flask (stream) handler which writes to stderr
  app.logger.setLevel(min_level)
  fh = logging.FileHandler(logfile_path)
  fh.setFormatter(formatter)
  app.logger.addHandler(fh)

  log_filter = CustomLogging.reset_log_filter('0.0.0.0')
  app.logger.addFilter(log_filter)
  app.logger.debug("Logging configured")

##---------------------------------------------------------------------------------------
def _cleanup(app):
  """ App-cleanup registered by atexit. Tear down any data-handler resources"""
  if hasattr(app, 'cve_dh'):
    print("Cleaning up data-handler resources...")
    app.cve_dh.resource_cleanup()

##---------------------------------------------------------------------------------------
def _register_blueprints(app):
  """Register all app blueprints"""

  ## Register routes from "api" blueprint object (bp_api)
  app.register_blueprint(bp_api)

  ## Register routes from "ui" blueprint object (bp_ui)
  ## FUTURE: app.register_blueprint(bp_ui)

##---------------------------------------------------------------------------------------
