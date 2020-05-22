"""

 Route mapping for the VESPA "api" blueprint.

"""
import json
from flask import Blueprint, request, current_app, jsonify

## Custom modules 
import cve_analysis 
import cve_data_abstraction
from api_authorization import api_authorize_get, api_authorize_post
from api_validation import api_data_validate

## Create blueprint object
blueprint_id = 'api'
bp_api = Blueprint(blueprint_id, __name__, template_folder="views")
setattr(bp_api, 'id', blueprint_id)

## Payload validaiton is performed by "jsonschema". jsonschema objects defined below are passed 
## to the ## @api_data_validation decorator. 
## jsonschema for /vuln method defines a list of "package-version-host" objects
d_schema_pvh = {
  'type': 'object',
  'properties': {
    'data': {
      'type': 'array',
      'items': { 
                  'type': 'object', 
                  'properties': {
                    'package': {'type': 'string'},
                    'version': {'type': 'string'},
                    'host': {'type': 'string'},
                  },
                  'required': ['package', 'version', 'host']
               },
    } 
  } 
}

api_version = 'v2.0'
##---------------------------------------------------------------------------------------
## POST request to identify software-packages that are vulnerable 
vuln_route = "/vespa/api/%s/vuln" % api_version
@bp_api.route(vuln_route,  methods=['POST'], endpoint='vuln' )
@api_data_validate(d_schema_pvh)
def check_vuln():
  """ Take input list of package-version-host objects and perform vulnerablity analysis""" 
  tag = "%s.check_vuln()" % blueprint_id
  d_pvh_data = request.get_json(force=True)

  l_pvh_data = d_pvh_data['data'] ## @api_data_validate has validated paylod format
 
  capp = current_app._get_current_object()
  capp.logger.debug("%s: Checking vulnerability of input package-version-host list" % (tag)) 

  d_result = cve_analysis.analyze_vulnerable_package_list(l_pvh_data, capp.cve_dh)  
 
  result = jsonify(d_result)
  return result

##---------------------------------------------------------------------------------------
## GET request to identify timestamp of last CVE storage update 
timestamp_route = "/vespa/api/%s/data/timestamp" % api_version
@bp_api.route(timestamp_route,  methods=['GET'], endpoint='timestamp' )
def data_timestamp():
  """ Get last update timestamp of CVE data """ 
  tag = "%s.data_timestamp()" % blueprint_id
  
  capp = current_app._get_current_object()

  dh = capp.cve_dh 

  storage_type = dh.storage_type

  timestamp = dh.data_timestamp()
  d_result = {'storage_type': storage_type, 'last_update': timestamp} 
  result = jsonify(d_result)
  return result

##---------------------------------------------------------------------------------------
## GET request to refresh data source 
refresh_route = "/vespa/api/%s/data/refresh" % api_version
@bp_api.route(refresh_route,  methods=['GET'], endpoint='refresh' )
@api_authorize_get 
def data_refresh():
  """ Re-initialize the CVE data-handler object """ 
  tag = "%s.data_refresh()" % blueprint_id
  
  capp = current_app._get_current_object()
  capp.logger.info("%s: Refreshing CVE data storage..." % (tag)) 

  dh = capp.cve_dh 

  status = dh.refresh_storage()
  d_result = {'status': status} 
  result = jsonify(d_result)
  return result

##---------------------------------------------------------------------------------------
