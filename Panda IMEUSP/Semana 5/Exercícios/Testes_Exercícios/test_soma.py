#nome da funcao de teste pode ser qualquer um
#nome da funcao correta que o arquivo irá fazer referência

import soma
def test_soma0():
    assert soma.soma(0,2) == 2

def test_soma1():
    assert soma.soma(1,2) == 3
    
def test_soma2():
    assert soma.soma(-1,5) == 4
