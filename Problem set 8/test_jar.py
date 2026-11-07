from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar_custom = Jar(5)
    assert jar_custom.capacity == 5

    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)
