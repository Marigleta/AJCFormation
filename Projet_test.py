
from unittest import result
from main import count_char, check_if_maj, check_if_special, check_if_valid_password

def test_count_char():
    input = "Bonjour"
    expected = 7
    result = count_char(input)
    assert expected == result


def test_check_if_maj():
    input1 = "Bonjour"
    input2 = "bonjour"
    input3 = "boNJour"

    expected1 = True
    expected2 = False
    expected3 = True

    result1 = check_if_maj(input1)
    result2 = check_if_maj(input2)
    result3 = check_if_maj(input3)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3

def test_check_if_special():
    input1 = "B!njour"
    input2 = "Bonjour"
    input3 = "Bonjo-r"

    expected1 = True
    expected2 = False
    expected3 = True

    result1 = check_if_special(input1)
    result2 = check_if_special(input2)
    result3 = check_if_special(input3)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3

def test_check_if_valid_password():
    input1 = "jour"
    input2 = "Bonjo-r"
    input3 = "bonjour"
    input4 = "Bonjourabc"


    expected1 = False
    expected2 = False
    expected3 = False
    expected4 = True

    result1 = check_if_valid_password(input1)
    result2 = check_if_valid_password(input2)
    result3 = check_if_valid_password(input3)
    result4 = check_if_valid_password(input4)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3
    assert expected4 == result4





