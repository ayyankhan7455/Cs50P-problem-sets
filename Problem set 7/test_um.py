import pytest
from um import count


def test_basic_count():
    assert count("um") == 1
    assert count("hello, um, world") == 1
    assert count("Um, thanks, um...") == 2


def test_substrings():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("instrument") == 0


def test_case_insensitivity():
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("Um, hello UM, um.") == 3
