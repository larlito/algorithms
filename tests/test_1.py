import pytest
from src.main import factorial

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (0,1),
                             (1,1),
                             (4,24),
                             (20,2432902008176640000)
                         ])

def test_factorial_positive(value1,extend_result):
    assert factorial(value1) == extend_result

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (-2,pytest.raises(ValueError)),
                             (2.3,pytest.raises(TypeError)),
                             ('asdf',pytest.raises(TypeError))

                         ])

def test_factorial_negative(value1,extend_result):
    with extend_result:
        assert factorial(value1) == extend_result