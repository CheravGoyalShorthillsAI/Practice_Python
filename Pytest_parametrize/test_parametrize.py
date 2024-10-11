# def test_eval_addition():
#     assert eval("2 + 2") == 4

# def test_eval_subtraction():
#     assert eval("2 - 2") == 0

# def test_eval_multiplication():
#     assert eval("2 * 2") == 4

# def test_eval_division():
#     assert eval("2 / 2") == 1.0


import pytest

@pytest.mark.parametrize("test_input, expected_output", [("2+2", 4), ("2-2", 0), ("2*2", 4), ("2/2", 1.0)])
def test_eval(test_input, expected_output):
    assert eval(test_input) == expected_output