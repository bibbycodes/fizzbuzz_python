from lib.fizzbuzz import fizzbuzz

def test_fizzbuzz_with_input_0():
  assert fizzbuzz(0) == 0

def test_fizzbuzz_with_input_1():
  assert fizzbuzz(1) == 1

def test_fizzbuzz_with_input_2():
    assert fizzbuzz(2) == 2

def test_fizzbuzz_with_input_3():
  assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_with_input_4():
  assert fizzbuzz(4) == 4

def test_fizzbuzz_with_input_5():
  assert fizzbuzz(5) == "buzz"

def test_fizzbuzz_with_input_6():
  assert fizzbuzz(6) == 'fizz'