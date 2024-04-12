import nltk
from nltk.translate import AlignedSent, IBMModel1, IBMModel2, IBMModel3, IBMModel4, IBMModel5

# Example bilingual sentence pairs (German to English)
bitext = [
    AlignedSent(['klein', 'ist', 'das', 'haus'], ['the', 'house', 'is', 'small']),
    AlignedSent(['das', 'haus', 'ist', 'ja', 'groß'], ['the', 'house', 'is', 'big']),
    AlignedSent(['das', 'buch', 'ist', 'ja', 'klein'], ['the', 'book', 'is', 'small']),
    AlignedSent(['das', 'haus'], ['the', 'house']),
    AlignedSent(['das', 'buch'], ['the', 'book']),
    AlignedSent(['ein', 'buch'], ['a', 'book'])
]

def test_ok_1():
    assert True == True, "Should be true"

def test_ok_2():
    IBMModel1(bitext, 5)

def test_ok_3():
    IBMModel2(bitext, 5)

def test_ok_4():
    IBMModel3(bitext, 5)

def test_ok_5():
    IBMModel4(bitext, 5)
    
def test_ok_6():
    IBMModel5(bitext, 5)

def test_violation_1():
    IBMModel1(bitext, 5, probability_tables={})

def test_violation_2():
    IBMModel2(bitext, 5, {})
    
def test_violation_3():
    IBMModel3(bitext, 5, probability_tables={})

def test_violation_4():
    IBMModel4(bitext, 5, {})

def test_violation_5():
    IBMModel5(bitext, 5, probability_tables={})