import pytest
from fuel import convert, gauge

def test_convert():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    assert convert("3/4") >= 75


def test_full():
    assert gauge(99) == "F"


def test_empty():
    assert gauge(1) == "E"


def test_percentage():
    assert gauge(55) == "55%"
