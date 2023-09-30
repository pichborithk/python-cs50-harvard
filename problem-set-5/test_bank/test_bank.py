from bank import value

def test_lowercase():
    assert value("hello") == 0


def test_uppercase():
    assert value("HELLO") == 0


def test_hey():
    assert value("hey") == 20


def test_whatsup():
    assert value("what's up?") == 100