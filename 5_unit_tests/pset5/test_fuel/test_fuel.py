from fuel import convert
from fuel import gauge


def test_convert():
    assert convert('3/4') == 75.0
    assert convert('1/2') == 50.0
    assert convert('1/5') == 20.0

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(75) == '75%'
    assert gauge(33) == '33%'

