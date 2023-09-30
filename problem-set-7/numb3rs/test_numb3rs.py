from numb3rs import validate

def test_ok():
    assert validate("127.0.0.1") == True

def test_greater():
    assert validate("275.3.6.100") == False
    assert validate("168.999.6.100") == False
    assert validate("168.192.610.100") == False
    assert validate("168.192.61.1001") == False


def test_negative():
    assert validate("100.0.-1.100") == False


def test_no_number():
    assert validate("cat") == False


def test_lack_number():
    assert validate("8.8.8") == False