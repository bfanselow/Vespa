"""

 File: test_version_math_exc.py 
 Description: 
    Unit tests on the version_math.is_version_in_window() functions for version inputs 
    that should raise exception.
    NOTE: We are ONLY testing invalid version inputs here. Testing of the (True|False)
    response from the function is is done by test_version_math.py 

"""

import pytest
import app.version_math as vm
from app.version_math import VersionError 

## list of (invalid-version-input,) tuples to be used in parameterization input
PARAM_TUPS = [ 
  ("1.2.1", "1.2.1", "1.2.1"),         # v_lo == v_hi
  ("0.0.0", "2.2.2", "1.1.1"),         # v_lo > v_hi
  ("0,0.10", "0.0.1", "0.1.1"),        # comma in place of dot
  ("0..0.10", "0.0.1", "0.1.1"),       # double dot
  ("v0.0.10", "0.0.1", "0.1.1"),       # alpha char
  ("v0.0.10", "0.0.1a6", "0.1.1-beta") # alpha char
]

##------------------------------------------------------------------------
@pytest.mark.parametrize("input_versions_tuple", PARAM_TUPS)
def test_exception_on_invalid_problem(input_versions_tuple):
    """ 
     Verify that we raise an VersionError() exception as expected with invalid version parameters 
    """ 
    with pytest.raises(VersionError):
        vm.is_version_in_window(*input_versions_tuple) 
