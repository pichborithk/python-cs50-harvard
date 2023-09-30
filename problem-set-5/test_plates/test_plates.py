from plates import is_valid

def test_legit():
    assert is_valid("AA1234") == True


def test_less_char():
    assert is_valid("A") == False


def test_exceed_requirment():
    assert is_valid("AAA1234") == False


def test_zero():
    assert is_valid("AA0123") == False


def test_number_in_between():
    assert is_valid("AA233A") == False


def test_not_alphabet_start():
    assert is_valid("12") == False


def test_symbol():
    assert is_valid("AB3.14") == False