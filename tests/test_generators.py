import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Тест на корректность выхода данных при наличии определенной валюты
@pytest.fixture()
def test_filter_by_currency():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "RUB"}}},
        {"operationAmount": {"currency": {"code": "RUB"}}},
    ]
    result =  [
        {"operationAmount": {"currency": {"code": "RUB"}}},
        {"operationAmount": {"currency": {"code": "RUB"}}},
    ]
    res = list(filter_by_currency(transactions, "RUB"))
    assert res == result

# Проверка обработки невалидных значений
@pytest.mark.parametrize("inp", ["", "abcd", 1234, None])
def test_invalid_input(inp):
    with pytest.raises(ValueError):
        list(filter_by_currency(inp))


# Проверка работы выдачи описаний транзакций
@pytest.fixture
def test_transaction_descriptions():
    descriptions_ = list_of_transactions
    result_descriptions = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"]
    exp = list(transaction_descriptions(descriptions_))
    assert exp == result_descriptions




# Тест на введенных невалидных значений
@pytest.mark.parametrize("inp", ["", "abcd", 1234, None])
def test_invalid_inp_desc(inp):
    with pytest.raises(ValueError):
        list(transaction_descriptions(inp))

# Проверки на работоспособность маскировки карт
def test_card_number_generator():
    gen_info = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]
    assert list(card_number_generator(1, 3)) == gen_info

def test_single_generator():
    gen_single = card_number_generator(50, 51)
    assert next(gen_single) == "0000 0000 0000 0050"


def test_start_greater_than_end():
    with pytest.raises(ValueError):
        list(card_number_generator(100, 50))

def test_end_max_generator():
    max_gen = 9999999999999999
    assert list(card_number_generator(max_gen, max_gen)) == ["9999 9999 9999 9999"]

