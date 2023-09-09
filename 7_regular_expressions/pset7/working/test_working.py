from working import convert
import pytest

def test_hours():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('6 AM to 1 PM') == '06:00 to 13:00'
    assert convert('12:00 PM to 9:00 PM') == '12:00 to 21:00'


def test_format():
    with pytest.raises(ValueError):
        convert('aaa')
    with pytest.raises(ValueError):
        convert('9:00 am to 5:00 pm')
    with pytest.raises(ValueError):
        convert('11:00 AM to 8 PM')


