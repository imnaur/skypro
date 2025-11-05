import json
from unittest.mock import mock_open, patch

from src.utils import read_json


def test_read_json_returns():
    """Тест с поддельными данными проверяет работоспособность оригинальной функции."""
    fake_data = [
        {"operationAmount": 100},
        {"operationAmount": 200},
        {"operationAmount": None},
        {"noAmount": True},
    ]
    with patch("builtins.open", mock_open(read_data=json.dumps(fake_data))):
        with patch("json.load", return_value=fake_data):
            res = read_json()
    assert res == [100, 200]
