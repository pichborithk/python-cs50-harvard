import pytest
from jar import Jar


def test_init():
    jar_1 = Jar()
    assert jar_1.capacity == 12
    jar_2 = Jar(5)
    assert jar_2.capacity == 5

def test_init_error():
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar(-100)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(6)
    assert jar.size == 9

def test_deposit_error():
    jar = Jar(2)
    with pytest.raises(ValueError):
        jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar.withdraw(3)
    assert jar.size == 7
    jar.withdraw(1)
    assert jar.size == 6

def test_withdraw_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(3)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(6)