import sys
sys.path.append('../')

import fizzbuzz_funcao as ff

def test_one():
 assert ff.fizzbuzz(9) == 'Fizz'

def test_two():
 assert ff.fizzbuzz(10) == 'Buzz'

def test_three():
 assert ff.fizzbuzz(15) == 'FizzBuzz'

def test_three():
 assert ff.fizzbuzz(4) == 4
