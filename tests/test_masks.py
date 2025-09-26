import pytest
from src.masks import get_mask_card_number, get_mask_account

# Проверка маскировки номера счета и номера карты
@pytest.mark.parametrize("inp, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567891011121", "1234 56** **** 1121")
])
def test_get_mask_card_number(inp, expected):
    assert get_mask_card_number(inp) == expected


# Проверка обработки нестандартного ввода
@pytest.mark.parametrize("inp", [
    "",
    "1234",
    "12345678901234567890",
    "abc12345de1234",
])
def test_get_mask_card_number_invalid(inp):
    with pytest.raises(ValueError):
        get_mask_card_number(inp)



