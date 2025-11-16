import json
from unittest.mock import Mock, mock_open, patch

from src.external_api import currency_transactions
from src.utils import read_json


def test_currency_transactions_with_mock():
    """Тест с поддельными данными проверяет работоспособность оригинальной функции."""
    fake_data = [
        {"operationAmount": {"amount": 100, "currency": {"code": "EUR"}}},
        {"operationAmount": {"amount": 439, "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": 50, "currency": {"code": "USD"}}},
    ]
    with patch("builtins.open", mock_open(read_data=json.dumps(fake_data))):
        with patch("json.load", return_value=fake_data):
            transactions = read_json()

    def mock_get(url, headers):
        mock_response = Mock()
        if "EUR" in url:
            mock_response.json.return_value = {"result": 110.00}
        elif "USD" in url:
            mock_response.json.return_value = {"result": 5000.00}
        else:
            mock_response.json.return_value = {"result": 0.0}
        return mock_response

    with patch("requests.get", side_effect=mock_get):
        results = [currency_transactions(t) for t in transactions]

    assert results == [110.00, 439.00, 5000.00]
