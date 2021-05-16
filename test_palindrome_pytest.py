import pytest
import palindrome

def test_1():
    assert palindrome.palin(1234) == "Input is not string"

def test_2():
    assert palindrome.palin("1234") == False

def test_3():
    assert palindrome.palin("545") == True

def test_4():
    assert palindrome.palin("asdsa") == True
