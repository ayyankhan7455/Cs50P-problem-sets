from plates import is_valid


def test_min_max_length():
    assert is_valid("A") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS50") == True


def test_start_with_two_letters():
    assert is_valid("50CS") == False
    assert is_valid("C50") == False
    assert is_valid("CS") == True


def test_number_placement():
    assert is_valid("CS50P") == False  # Number in the middle
    assert is_valid("CS05") == False  # First number cannot be 0
    assert is_valid("CS50") == True


def test_punctuation_and_spaces():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS!50") == False
