import pytest
import pyDOE as doe

def test_fullfact_numpy_float64_issue():
    doe.fullfact([2]*3)
