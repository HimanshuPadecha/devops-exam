import pytest
from calc import calculator

def test_answer():
    assert calculator(10,20,"+") == 30
    assert calculator(20,10,"-") ==  10
    assert calculator(20,10,"*" ) == 200
    assert calculator(30,10,"/") == 3