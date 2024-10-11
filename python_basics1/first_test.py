import pytest

def func(x):
    return x+5

@pytest.mark.one
def test_method1():
    assert func(3) == 8
    

@pytest.mark.two
def test_method2():
    x=10
    y=10
    assert x==y


def test_method3():
    a=15
    b=20
    assert a+5==b