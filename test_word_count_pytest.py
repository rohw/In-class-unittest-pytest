import pytest
import word_count

def test_1():
    assert word_count.w_count(1234) == "Input is not string"

def test_2():
    assert word_count.w_count("hi") == 1

def test_3():
    assert word_count.w_count("Hi my name is Wonjun") == 5