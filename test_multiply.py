from intial import multiply
import pytest


@pytest.mark.parametrize(
    ('input_n','expected'),
    
    (

    (3,6),
    (5.,10.)

    )
)

def test_multiplyfunc(input_n,expected):

    assert multiply(input_n) == expected
    assert multiply(input_n) == expected