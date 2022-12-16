"""testing coverage"""

from foobar.bar.a import func
from foobar.foo.a import identity


def test_increment():
    """test adding"""
    assert func(4) == 5
    assert func(5) == 6

def test_no_increment():
    """ test does not increment """
    assert func(0) != 1
    assert func(3) != 4
    assert func(6) != 7

def test_identity():
    """ verify """
    assert identity(-1) == -1
    assert identity(0) == 0
    assert identity(1) == 1
