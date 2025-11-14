from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Определяет, карта это или счет, и маскирует с сохранением текста."""
    digits = "".join(i for i in card_number if i.isdigit())
    if len(digits) == 16:
        return card_number[:-16] + get_mask_card_number(digits)
    elif len(digits) == 20:
        return card_number[:-20] + get_mask_account(digits)
    raise ValueError("Введите корректный номер карты: 16 цифр или счета: 20 цифр")


def get_date(date_info: str) -> str:
    """Функция, которая возвращает правильный формат даты."""
    correct_date = "".join(i for i in date_info if i.isdigit())
    if len(date_info) < 8:
        raise ValueError("Введите корректные данные")
    changed_date = correct_date[:8]
    year = changed_date[:4]
    month = changed_date[4:6]
    day = changed_date[6:8]
    return f"{day}.{month}.{year}"
