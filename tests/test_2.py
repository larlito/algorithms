import pytest
from src.main import fibonacci

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (0,[0]),
                             (5,[0,1,2,3,4,5]),

                         ])

def test_fibonacci_positive(value1,extend_result):
    assert fibonacci(value1) == extend_result

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (-2,pytest.raises(ValueError)),
                             (11.1,pytest.raises(TypeError)),
                             ('121',pytest.raises(TypeError))

                         ])

def test_fibonacci_negative(value1,extend_result):
    with extend_result:
        assert fibonacci(value1) == extend_result