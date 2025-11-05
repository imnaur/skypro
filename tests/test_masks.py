import pytest

from src.masks import get_mask_account, get_mask_card_number


# Проверка маскировки номера карты
@pytest.mark.parametrize(
    "inp, expected", [("7000792289606361", "7000 79** **** 6361"), ("1234567891011121", "1234 56** **** 1121")]
)
def test_get_mask_card_number(inp: str, expected: str) -> None:
    assert get_mask_card_number(inp) == expected


# Проверка обработки нестандартного ввода
@pytest.mark.parametrize(
    "inp",
    [
        "",
        "1234",
        "12345678901234567890",
        "abc12345de1234",
    ],
)
def test_get_mask_card_number_invalid(inp: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(inp)


# Проверка маскировки номера счета
# Валидные случаи
@pytest.mark.parametrize(
    "account, expected",
    [
        ("12345678901234567890", "**7890"),
        ("00000000000000000001", "**0001"),
        ("98765432109876543210", "**3210"),
    ],
)
def test_get_mask_account_valid(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected


# Невалидные случаи
@pytest.mark.parametrize(
    "account",
    [
        "",  # пустая строка
        "12345678",  # меньше 20 цифр
        "123456789012345678901",  # больше 20 цифр
        "abcd5678901234567890",  # буквы в номере
    ],
)
def test_get_mask_account_invalid(account: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account)
