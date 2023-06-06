from src.counter import count_ocurrences
from unittest.mock import mock_open, patch
import pytest


@pytest.fixture(scope="session")
def fake_data():
    return "python cs Python Cs PYTHON"


def test_counter(fake_data):
    with patch("builtins.open", mock_open(read_data=fake_data)):
        assert count_ocurrences("", "python") == 3
        assert count_ocurrences("", "cs") == 2
