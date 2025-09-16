def mask_account_card(card_number: str) -> str:
    """"Функция, которая маскирует данные карты или счета."""
    if "Счет" in card_number:
        return "Счет " + "**" + card_number[-4:]
    elif "Maestro" or "Mastercard" or "Visa" in card_number:
        masked_num = card_number[-16:]
        start_num = masked_num[:6]
        stars_num = "*" * 6
        end_num = masked_num[-4:]
        finish_num = start_num + stars_num + end_num
        card_number_result = " ".join(finish_num[i : i + 4] for i in range(0, len(masked_num), 4))
    return card_number[:-16] + card_number_result


def get_date(date_info: str) -> str:
    """Функция, которая возвращает правильный формат даты."""
    changed_date = date_info[:10]
    correct_date = changed_date.replace("-", "")
    day_date = correct_date[-2:]
    month_date = correct_date[-4:-2]
    year_date = correct_date[:4]
    return f"{day_date}.{month_date}.{year_date}"
