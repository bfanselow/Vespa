"""
 
 File: test_version_math.py
 Description: 
    Unit-testing on the version_math.is_version_in_window() functions.
    NOTE: We do NOT test for invalid input exceptions here. This is done by: test_version_math_exc.py 
 
"""
import pytest
import app.version_math as vm


## tuple of ((version, version_lo, version_hi), result) to be used in parameterization input
PARAM_TUPS =  [ 
 ( ("0", "1", "2"),             False), 
 ( ("0.0", "0.1", "0.2"),       False), 
 ( ("0.0.0", "0.0.1", "0.0.2"), False),
 
 ( ("0", "0", "2"),             True), 
 ( ("0.1", "0.1", "0.2"),       True), 
 ( ("0.0.1", "0.0.1", "0.0.2"), True), 

 ( ("1", "0", "2"),             True), 
 ( ("0.1", "0.0", "0.2"),       True), 
 ( ("0.0.1", "0.0.0", "0.0.2"), True), 

 ( ("2", "0", "2"),             False), 
 ( ("0.2", "0.0", "0.2"),       False), 
 ( ("0.0.2", "0.0.0", "0.0.2"), False), 

 ( ("0.8.0", "0.8", "1.0"),      True),
 ( ("0.8.1", "0.8", "1.0"),      True),
 ( ("0.8.99", "0.8", "1.0"),     True),
 ( ("0.999.999", "0.8", "1.0"),  True),
 ( ("0.0.10", "0.0.1", "0.1.1"), True),

 ( ("100.0001", "100.0002", "101.0"), False), 
 ( ("0.9999", "0.9998", "1.0"),       True), 
 ( ("1.999", "1.1", "1.998"),         False), 
]

##------------------------------------------------------------------------
@pytest.mark.parametrize("input_versions_tuple, exp_result", PARAM_TUPS)
def test_compute(input_versions_tuple, exp_result):
    """ 
      Test computuation of various math operations from parameterized input
    """ 
    result = vm.is_version_in_window(*input_versions_tuple)
    assert (result == exp_result) 
