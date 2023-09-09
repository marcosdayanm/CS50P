import seasons
from datetime import date
import pytest
import sys

today = date.today()

def test_vali_date():
    assert seasons.vali_date(date.today(), '2022-12-23') == (today, date(2022,12,23))
    assert seasons.vali_date(date.today(), '2003-04-04') == (today, date(2003,4,4))

    with pytest.raises(SystemExit) as exc_info:
        seasons.vali_date(today, '2023-12-23')
    assert str(exc_info.value) == 'Invalid date'

    with pytest.raises(SystemExit) as exc_info:
        seasons.vali_date(today, 'apple')
    assert str(exc_info.value) == 'Invalid date'

    with pytest.raises(SystemExit) as exc_info:
        seasons.vali_date(today, '2023-123-23')
    assert str(exc_info.value) == 'Invalid date'

    with pytest.raises(SystemExit) as exc_info:
        seasons.vali_date(today, '2023-12-35')
    assert str(exc_info.value) == 'Invalid date'



def test_calc_mins():
    assert seasons.calc_mins(today, date(2022,12,23)) == 313920
    assert seasons.calc_mins(today, date(2003,4,4)) == 10686240


def test_num_text():
    assert seasons.num_text(10686240) == 'Ten million, six hundred eighty-six thousand, two hundred forty minutes'
    assert seasons.num_text(29409120) == 'Twenty-nine million, four hundred nine thousand, one hundred twenty minutes'
    assert seasons.num_text(25005600) == 'Twenty-five million, five thousand, six hundred minutes'
