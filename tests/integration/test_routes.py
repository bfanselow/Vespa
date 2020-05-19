"""

 File: test_flask_routing.py
 Description:
  Test the Vespa Flask routing for expected responses (for success and failures) 
  Uses a Flask-app "test_client" fixture created in tests/integration/conftest.py

 !!!!!
 NOTE: This module does NOT check for exceptions raised on invalid requests as this 
       "test_client" returns the reponses prior to our @app.errorhandler() methods defined 
       in "vespa_flask.py" which format the exceptions into JSON responses. 
       To validate these formatted exception responses, use the functional-testing scripts 
       in tests/functional/* 
 !!!!!

"""
import json
import pytest
from config import *

api_key = TestingConfig.API_KEY
version = TestingConfig.VERSION

RESOURCE_BASE = "/vespa/api/v%s" % version

RESOURCE_VULN = RESOURCE_BASE + '/vuln' 
RESOURCE_REFRESH = RESOURCE_BASE + '/data/refresh' 
RESOURCE_TIMESTAMP = RESOURCE_BASE + '/data/timestamp' 

## valid post payload
PAYLOAD = { 'data':
 [{"package": "freeciv", "version": "1.4.0", "host": "330facf12c55432d9f7eed27c5448ac8.example.org"}, {"package": "mint-linux", "version": "2016.3.0", "host": "330facf12c55432d9f7eed27c5448ac8.example.org"}]
}

##-----------------------------------------------------------------------------
## Helper methods
##-----------------------------------------------------------------------------
def response_to_json(response):
    """Convert Decoded response to json"""
    return json.loads(response.data.decode('utf8'))

def post_json(client, url, payload_dict):
    """POST jsonified dict to specified url """
    return client.post(url, data=json.dumps(payload_dict), content_type='application/json')

##-----------------------------------------------------------------------------
## TESTS
##-----------------------------------------------------------------------------
def test_resource_not_found(test_client):
    """
     Check proper handling/response of 404
    """
    response = test_client.get('/bogus')
    assert response.status_code == 404 

##-----------------------------------------------------------------------------
def test_valid_data_refresh(test_client):
    """
     Check proper handling/response from "GET /vespa/api/<version>/data/refresh" 
    """
    response = test_client.get(RESOURCE_REFRESH, headers={'X-Api-Key': api_key})
    assert response.status_code == 200 
    assert response_to_json(response) == {"status":True} 

##-----------------------------------------------------------------------------
def test_invalid_data_refresh_method(test_client):
    """
     Check proper (405) response from (WRONG method-type)  "POST /vespa/api/<version>/data/refresh" 
     (See "tests/functional/curl_request_failures.sh" for testing invalid api-key)
    """
    response = test_client.post(RESOURCE_REFRESH, headers={'X-Api-Key': api_key})
    assert response.status_code == 405

##----------------------------------------
def test_valid_data_timestamp(test_client):
    """
     Check proper handling/response of /data/timestamp 
    """
    response = test_client.get(RESOURCE_TIMESTAMP)
    assert response.status_code == 200

##----------------------------------------
def test_invalid_vuln_post(test_client):
    """
     Check proper handling/response of invalid post: 400 Bad Request 
    """
    response = test_client.post(RESOURCE_VULN, data=dict())
    assert response.status_code == 400

##----------------------------------------
def test_valid_vuln_post1(test_client):
    """
     Check proper handling/response of valid POST
    """
    response = post_json(test_client, RESOURCE_VULN, PAYLOAD)
    assert response.status_code == 200 
