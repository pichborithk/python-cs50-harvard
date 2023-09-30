from twttr import shorten

def test_lowercase():
    assert shorten("Hi") == "H"
    assert shorten("Hello World") == "Hll Wrld"


def test_uppercase():
    assert shorten("HI") == "H"


def test_number():
    assert shorten("hi 5") == "h 5"


def test_punctuation():
    assert shorten("what's up?") == "wht's p?"