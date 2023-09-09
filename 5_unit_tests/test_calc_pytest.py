import pytest
from calculator import square

def test_positive():
    assert square(2) == 4

def test_negative():
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0



def test_string():  # de ésta manera estamos diciéndole a pytest que aunque ésto pueda dar un error, lo consideremos correcto
    with pytest.raises(TypeError):
        square('cat')
