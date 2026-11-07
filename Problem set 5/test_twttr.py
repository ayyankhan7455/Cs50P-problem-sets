from twttr import shorten


def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""


def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""


def test_mixed():
    assert shorten("TwitTeR") == "TwtTR"


def test_numbers():
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("CS50, world!") == "CS50, wrld!"
