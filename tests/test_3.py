import pytest
from src.main import count_ones

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (11,1),
                             (0,0),
                             (1,0),
                             (19291293192394,4),
                             (-5,0)


                         ])

def test_count_ones_positive(value1,extend_result):
    assert count_ones(value1) == extend_result

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (11.1,pytest.raises(TypeError)),
                             ('121',pytest.raises(TypeError))

                         ])

def test_count_ones_negative(value1,extend_result):
    with extend_result:
        assert count_ones(value1) == extend_result