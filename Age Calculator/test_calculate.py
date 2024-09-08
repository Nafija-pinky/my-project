import pytest
from calculate import judge_leap_year, month_days

def test_judge_leap_year():
    assert judge_leap_year(2020) == True
    assert judge_leap_year(2021) == False
    assert judge_leap_year(1900) == False
    assert judge_leap_year(2000) == True

def test_month_days():
    assert month_days(1, False) == 31
    assert month_days(2, False) == 28
    assert month_days(2, True) == 29
    assert month_days(4, False) == 30
    assert month_days(7, False) == 31

