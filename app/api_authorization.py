"""

  Module: api_authorization.py
  Description: 
   API authorization based on simple api-key validation to be used by the API endpoints.  
   Provides decorators (@api_authorize_get and (@api_authorize_post) for authorization
   of each method type.  

  Usage: Use as a route decorator for api-methods needing immediate input validation.
  Example:
     @api_blueprint.route("/api/v1.0/data/refresh",  methods=['GET'])
     @api_authorize_get
     def data_refresh():
     ...

  Notes: to use the same api_authorization() decorator on multiple routes you must include
         specify uniq endpoint=<endpoint> names in the route() args
 
"""
import json

## Flask modules
from functools import wraps
from flask import request, current_app

API_KEY_HEADER_NAME = 'X-Api-Key'
API_KEY_POST_NAME = 'API-KEY'
##-----------------------------------------------------------------------------------------
class ApiAuthorizationError(Exception):
  pass

##-----------------------------------------------------------------------------------------
def validate_api_key(request_key):
  """
    Validate API-key. Can be in payload or HEADERS
    Required Args:
      1) request_key (str): API-key extracted form either GET headers or POST payload 
    Raises: ApiAuthorizationError if validation error.
  """
  valid_api_key = current_app.config['API_KEY'] 

  if not request_key:
    raise ApiAuthorizationError("API request authorization failed: no api-key in payload or headers")

  if request_key != valid_api_key:
    raise ApiAuthorizationError("API request authorization failed - Invalid API-Key: (%s)" % (request_key))

##-----------------------------------------------------------------------------------------
def api_authorize_get(func):
  """
    Decorator function for route functions needing api-key validation from GET requests.
    Expects flask.request object in JSON format from POST request. 
    Raises: ApiAuthorizationError if validation error.
  """
  @wraps(func)
  def wrapper(**kwargs):
    tag = 'api_authorize'
    ##print( "\nSTART DECORATOR: validate_payload %s" % (str(kwargs)))
    if request is None: 
      raise ApiAuthorizationError("%s: Empty request object" % (tag))

    api_key = request.headers.get(API_KEY_HEADER_NAME)
    try:
      validate_api_key(api_key)
    except Exception as e:
      raise

    ret = func(**kwargs)
    ##print( "END DECORATOR: return %s\n" % (ret))
    return ret 
  return wrapper

##-----------------------------------------------------------------------------------------
def api_authorize_post(func):
  """
    Decorator function for route functions needing api-key validation from POST requests.
    Raises: ApiAuthorizationError if validation error.
  """
  @wraps(func)
  def wrapper(**kwargs):
    tag = 'api_authorize'
    ##print( "\nSTART DECORATOR: validate_payload %s" % (str(kwargs)))
    if request is None: 
      raise ApiAuthorizationError("%s: Empty request object" % (tag))
    d_payload = request.get_json(force=True) 
    ##print("PAYLOAD: %s" % str(d_payload))
    try:
      json_payload = json.dumps(d_payload)
    except Exception as e:
      raise ApiAuthorizationError("%s: Request payload is not valid json: %s" % (tag, e))

    api_key = d_payload.get(API_KEY_POST_NAME, None)
    try:
      validate_api_key(api_key)
    except Exception as e:
      raise

    ret = func(**kwargs)
    ##print( "END DECORATOR: return %s\n" % (ret))
    return ret 
  return wrapper
