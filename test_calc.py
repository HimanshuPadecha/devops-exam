import pytest
from calc import calculator

a = input("Enter no")
b = input("Enter no")

operation = input("Enter operation : ")


assert calculator(10,20,"+") == 30
assert calculator(20,10,"-") ==  10
assert calculator(20,10,"*" ) == 200
assert calculator(30,10,"/") == 3