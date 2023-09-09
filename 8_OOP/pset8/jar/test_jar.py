from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == '🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    jar.deposit(2)
    assert jar.quantity == 7
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(5)
    assert jar.quantity == 4
    with pytest.raises(ValueError):
        jar.withdraw(6)

