from unittest.mock import patch

import pandas as pd

from src.reading_files import reading_csv, reading_excel


@patch("pandas.read_csv")
def test_reading_csv(mock_read_csv):
    """Тест проверяет работоспособность функции чтения CSV файла."""
    mock_read_csv.return_value = pd.DataFrame([{"id": 55446, "transaction": 1766.99, "currency": "USD"}])
    result_csv = reading_csv("fake_patch.csv", sep=";")
    assert result_csv == [{"id": 55446, "transaction": 1766.99, "currency": "USD"}]
    mock_read_csv.assert_called_once_with("fake_patch.csv", sep=";")


@patch("pandas.read_excel")
def test_reading_excel(mock_read_excel):
    """Тест проверяет работоспособность функции чтения EXCEL файла."""
    mock_read_excel.return_value = pd.DataFrame([{"id": 6677, "transaction": 0, "currency": "RUB"}])
    result_excel = reading_excel("fake_patch.xlsx")
    assert result_excel == [{"id": 6677, "transaction": 0, "currency": "RUB"}]
    mock_read_excel.assert_called_once_with("fake_patch.xlsx", engine="openpyxl")
