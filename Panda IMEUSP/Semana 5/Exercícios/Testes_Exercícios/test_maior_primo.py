import sys
sys.path.append('../')

import maior_primo as mp



def test_one():
    assert mp.éPrimo(2) == True

def test_two():
    assert mp.éPrimo(3) == True
    


def test_three():
    assert mp.maior_primo(100) == 97

def test_four():
    assert mp.maior_primo(7) == 7
