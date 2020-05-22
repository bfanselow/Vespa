"""
 
  Module: api_validation.py
  Description: 
   Very simple data validation functions to be used by the API endpoints. 
   Primary module function is DECORATOR: @api_data_validate

  Usage: Use as a route decorator AFTER @api_authorize decorator. 
  Example:
     @api_blueprint.route("/api/v1.0/vuln/",  methods=['POST'])
     @api_authorize
     @api_data_validate
     def check_vuln():
     ...

  Notes: to use the same api_data_validate() decorator on multiple routes you must include
         specify uniq endpoint=<endpoint> names in the route() args
 
"""
import json
import jsonschema

## Flask modules
from functools import wraps
from flask import request, current_app

##-----------------------------------------------------------------------------------------
class ApiDataError(Exception):
  pass

##-----------------------------------------------------------------------------------------
def api_data_validate(d_json_schema):
  """
   Decorator function for API request payload schema validation. Must be positioned AFTER @api_authorize.
     Uses jsonschema to validate that the request data from API payload has valid top-level parameters.
   Required Arg: jsonschema object in dict format. 
   Raises: ApiDataError if validation error
   Return True
  """
  def data_validate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      if request is None: 
        raise ApiDataError("Empty request payload")
      d_payload = request.get_json(force=True) 

      try:
        jsonschema.validate(d_payload, d_json_schema)
      except jsonschema.exceptions.ValidationError as e:
        if "error" in e.schema:
          err = e.schema["error"]
        else:
          err = "%s: %s" % ( '.'.join(map(str,list(e.absolute_path))), e.message)
        raise ApiDataError("Invalid request payload: %s" % (err))
      except Exception as e:
        raise ApiDataError("Invalid request payload - Unexpected jsonschema exception: %s" % (e))
        raise
 
      ret = func(*args, **kwargs)
      return ret 
    return wrapper
  return data_validate 
