from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO, Newman") == 0


def test_h_start():
    assert value("Hi") == 20
    assert value("hey there") == 20
    assert value("HOWDY") == 20


def test_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("12345") == 100

