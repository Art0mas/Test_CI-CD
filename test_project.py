from project import *

def Test_Add():
    assert Add(2, 3) == 5

def Test_Factorial():
    assert Factorial(0) == 1
    assert Factorial(4) == 24

def Test_Average():
    assert Average([1, 2, 3, 4]) == 2.5
    assert Average([]) == 0

def Test_Reverse():
    assert Reverse_text("abc") == "cba"

