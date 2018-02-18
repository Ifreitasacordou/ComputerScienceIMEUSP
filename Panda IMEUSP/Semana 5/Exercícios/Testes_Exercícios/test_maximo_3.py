import sys
sys.path.append('../')

import maximo_3 as m3

def test_one():
    assert m3.maximo(30,14,10) == 30

def test_two():
    assert m3.maximo(0,-1, 1) == 1
