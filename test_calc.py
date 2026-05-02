import pytest
from calc import calculator


assert calculator(10,20,"+") == 30
assert calculator(20,10,"-") ==  10
assert calculator(20,10,"*" ) == 200
assert calculator(30,10,"/") == 3