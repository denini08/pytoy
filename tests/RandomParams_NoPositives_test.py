import random
# random.lognormvariate(mu, sigma) -> mu can have any value, and sigma must be greater than zero.
# random.vonmisesvariate(mu, kappa) ->  kappa must be greater than or equal to zero.
 

def test_ok_1():
    random.lognormvariate(0, 1)

def test_ok_2():
    random.vonmisesvariate(0, 1)

def test_ok_3():
    random.vonmisesvariate(0, 0)

def test_violation_1():
    random.lognormvariate(0, 0)

def test_violation_2():
    random.vonmisesvariate(0, -1)

def test_violation_3():
    random.vonmisesvariate(0, -10)