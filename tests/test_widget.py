import pytest

from src.widget import get_date, mask_account_card


# Проверка обработки ввода номера счетов и карт
# Тестирование корректности работы функции с разными вводными данными
@pytest.mark.parametrize(
    "inp, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", ""),
    ],
)
def test_mask_account_card(inp: str, expected: str) -> None:
    assert mask_account_card(inp) == expected


# Проверка обработки ввода невалидных данных
@pytest.mark.parametrize("inp", ["", "1234", "abcd", "53546488288645363672526273838393"])
def test_mask_account_card_invalid(inp: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(inp)


# Проверка обработки вводных дат
# Тестирование правильности преобразования невалидных даты
@pytest.mark.parametrize(
    "inp",
    [
        "",
        "1234",
        "abcd",
    ],
)
def test_get_date_invalid(inp: str) -> None:
    with pytest.raises(ValueError):
        get_date(inp)


# Тестирование правильности преобразования валидных даты
@pytest.mark.parametrize(
    "inp, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022.04.06", "06.04.2022"),
        ("2025/12/04", "04.12.2025"),
        ("2022.06.03", "03.06.2022"),
    ],
)
def test_get_date_valid(inp: str, expected: str) -> None:
    assert get_date(inp) == expected
