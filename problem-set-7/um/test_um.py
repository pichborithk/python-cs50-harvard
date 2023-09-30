from um import count


def test_without_anything():
    assert count("um") == 1
    assert count("hello um") == 1
    assert count("um um um") == 3


def test_case_sensitive():
    assert count("Um") == 1
    assert count("Um uM Um") == 3


def test_with_noncharacter():
    assert count("hello um,") == 1
    assert count("Um, thanks, um...") == 2


def test_word_with_um():
    assert count("drum") == 0
    assert count("um album") == 1
