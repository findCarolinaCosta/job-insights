from src.brazilian_jobs import read_brazilian_file
from unittest.mock import mock_open, patch
import pytest


@pytest.fixture(scope="session")
def fake_data():
    return """titulo,salario,tipo
Maquinista,2000,trainee"""


def test_brazilian_jobs(fake_data):
    with patch("builtins.open", mock_open(read_data=fake_data)):
        assert read_brazilian_file("") == [
            {
                "title": "Maquinista",
                "salary": "2000",
                "type": "trainee",
            }
        ]
