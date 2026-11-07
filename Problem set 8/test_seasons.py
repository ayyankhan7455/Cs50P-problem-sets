from datetime import date
import pytest
from seasons import parse_date, calculate_age_in_minutes


def test_parse_date():
    assert parse_date("2020-01-01") == date(2020, 1, 1)
    assert parse_date("1995-12-25") == date(1995, 12, 25)

    with pytest.raises(ValueError):
        parse_date("January 1, 2020")
    with pytest.raises(ValueError):
        parse_date("2020/01/01")
    with pytest.raises(ValueError):
        parse_date("not-a-date")


def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes(date(2019, 1, 1), date(2020, 1, 1)) == 525600
    assert calculate_age_in_minutes(date(2020, 1, 1), date(2021, 1, 1)) == 527040
