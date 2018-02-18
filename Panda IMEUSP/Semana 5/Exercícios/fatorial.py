def fatorial(x):
    if x < 0:
        return 0
    i = x
    f = 1
    while i > 0:
        f *= i
        i -= 1
    return f

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial1_negativo():
    assert fatorial(-10) == 0

def test_fatorial14():
    assert fatorial(4) == 24

def test_fatorial15():
    assert fatorial(5) == 120

