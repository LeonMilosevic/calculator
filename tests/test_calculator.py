def test_result():
    new_calculator = Calculator(5)
    assert new_calculator.result == 5

def test_add():
    new_calculator = Calculator(5)
    assert new_calculator.add(10) == 15

def test_substract():
    new_calculator = Calculator(5)
    assert new_calculator.substract(5) == 0

def test_multiply():
    new_calculator = Calculator(5)
    assert new_calculator.multiply(10) == 50

def test_devide():
    new_calculator = Calculator(5)
    assert new_calculator.devide(5) == 1

def test_sqrt():
    new_calculator = Calculator(9)
    assert new_calculator.sqrt() == 3

def test_reset_result():
    new_calculator = Calculator(5)
    assert new_calculator.reset_result() == 0