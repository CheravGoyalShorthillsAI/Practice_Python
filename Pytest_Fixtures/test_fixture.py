import pytest

# Define a fixture
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]

# Use the fixture in a test function
def test_sum(sample_data):
    assert sum(sample_data) == 10
