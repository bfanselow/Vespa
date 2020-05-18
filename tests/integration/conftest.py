"""

  File:
  Description:
   Defines a pytest fixture for creation of the Flask application
   to be used by tests/integration/test_*

"""
import sys
import pytest

sys.path.append('./app')
import app_factory
from config import *

##-----------------------------------------------------------------------
@pytest.fixture(scope='module')
def test_client():
    d_init = { 'config_class': TestingConfig }
    app = app_factory.create_app(d_init)
 
    # Expose the Werkzeug test Client 
    testing_client = app.test_client()
 
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
    yield testing_client  
    ctx.pop()
