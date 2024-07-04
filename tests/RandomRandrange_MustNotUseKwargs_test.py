import random


def test_ok_1():
    random.randrange(10)
    random.randrange(10, 100)

def test_ok_2():
    random.randrange(55)
    random.randrange(0, 30)

def test_ok_3():
    random.randrange(10, 12)
    random.randrange(-131231, 55)

def test_violation_1():
    random.randrange(10, step=1) 

def test_violation_2():
    random.randrange(start=10, stop=100)

def test_violation_3():
    random.randrange(start=55, step=1)
    