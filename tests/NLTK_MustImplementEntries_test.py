import nltk
from nltk.translate import AlignedSent, IBMModel2

# Example bilingual sentence pairs (German to English)
bitext = [
    AlignedSent(['klein', 'ist', 'das', 'haus'], ['the', 'house', 'is', 'small']),
    AlignedSent(['das', 'haus', 'ist', 'ja', 'groß'], ['the', 'house', 'is', 'big']),
    AlignedSent(['das', 'buch', 'ist', 'ja', 'klein'], ['the', 'book', 'is', 'small']),
    AlignedSent(['das', 'haus'], ['the', 'house']),
    AlignedSent(['das', 'buch'], ['the', 'book']),
    AlignedSent(['ein', 'buch'], ['a', 'book'])
]

# Create and train the IBM Model 1


def test_ok_1():
    assert True == True, "Should be true"

def test_ok_2():
    IBMModel2(bitext, 5)

def test_violation_1():
    IBMModel2(bitext, 5, probability_tables={})
    