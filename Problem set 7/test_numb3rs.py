from numb3rs import validate

def test_format():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat.dog.bird.fish") == False

def test_range():
    assert validate("275.3.6.28") == False
    assert validate("256.0.0.0") == False
    assert validate("0.0.0.256") == False
    assert validate("-1.0.0.0") == False
