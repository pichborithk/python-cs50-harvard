import pytest
from seasons import MinuteOfDate

def test_wrong_format():
    with pytest.raises(ValueError):
        MinuteOfDate("1990/10/11")
    with pytest.raises(ValueError):
        MinuteOfDate("January 1, 1999")
    with pytest.raises(ValueError):
        MinuteOfDate("01-01-1990")

