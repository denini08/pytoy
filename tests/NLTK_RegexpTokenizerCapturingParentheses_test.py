from nltk.tokenize import RegexpTokenizer

def test_ok_1():
    assert True == True, "Should be true"

def test_ok_2():
    RegexpTokenizer(r'(\w+)|([^\w\s]+)')

def test_violation_1():
    RegexpTokenizer(r'(?:\w+)|(?:[^\w\s]+)')