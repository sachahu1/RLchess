import pytest

from rlchess.utils.slot_utils import is_even

@pytest.mark.parametrize(
  "number,expected", [
    (2, True),
    (3, False),
    (64, True),
    (0, True),
    (1, False),
    (-5, False),
    (-2, True),
  ]
)
def test_is_even(number, expected):
  assert is_even(number) == expected
