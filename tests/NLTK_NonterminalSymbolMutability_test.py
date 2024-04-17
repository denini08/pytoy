from nltk.tokenize.util import regexp_span_tokenize
from nltk import CFG, Nonterminal, Production

def test_ok_1():
    assert True == True, "Should be true"

def test_ok_2():
    # Define the nonterminal and grammar
    A = Nonterminal('A')
    grammar = CFG(
        start=A,
        productions=[
            Production(A, ['a'])
        ]
    )

    print(grammar.productions(lhs=A))  # Expected to show "A -> 'a'"



def test_ok_3():
    class A:
        prop = 'A'

        def __hash__(self):
            return hash(self.prop)

    a = A()
    nonterminal = Nonterminal(a)
    nonterminal.symbol()

def test_violation_1():
    # Define the nonterminal and grammar
    A = Nonterminal('A')
    grammar = CFG(
        start=A,
        productions=[
            Production(A, ['a'])
        ]
    )

    print(grammar.productions(lhs=A))  # Expected to show "A -> 'a'"

    # Mutating the nonterminal symbol
    A._symbol = 'B'

    # Attempt to use the grammar after mutation
    print(grammar.productions(lhs=A))  # Might still show "B -> 'a'", but it's incorrect usage


def test_violation_2():
    class A:
        prop = 'A'

        def __hash__(self):
            return hash(self.prop)

    a = A()
    nonterminal = Nonterminal(a)
    nonterminal.symbol()

    # mutate the symbol
    a.prop = 'B'

    nonterm = nonterminal.symbol()