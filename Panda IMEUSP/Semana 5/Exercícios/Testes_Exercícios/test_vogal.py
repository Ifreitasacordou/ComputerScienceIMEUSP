import sys

sys.path.append('../')

import vogais

def test_one():
    assert vogais.vogal('a') == True
    
def test_two():
    assert vogais.vogal('e') == True

def test_three():
    assert vogais.vogal('i') == True
    
def test_four():
    assert vogais.vogal('o') == True

def test_five():
    assert vogais.vogal('u') == True
    
def test_five():
    assert vogais.vogal('A') == True

def test_six():
    assert vogais.vogal('b') == False

def test_seven():
    assert vogais.vogal('c') == False

