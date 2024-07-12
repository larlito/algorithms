import pytest
from src.main import pallindrome

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (0,True),
                             (123,False),
                             (121,True)

                         ])

def test_pallindrome_positive(value1,extend_result):
    assert pallindrome(value1) == extend_result

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (-2,pytest.raises(ValueError)),
                             (9.3,pytest.raises(TypeError)),
                             ('aaaa',pytest.raises(TypeError))

                         ])

def test_pallindrome_negative(value1,extend_result):
    with extend_result:
        assert pallindrome(value1) == extend_result