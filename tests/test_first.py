import pytest
from optan.examples import (
    load_data
)


def divide(x, y):
    return x / y


def test_raises():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)


def test_examples():
    ret = load_data.main()
    assert ret == 'finished'
