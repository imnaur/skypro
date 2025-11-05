def get_mask_card_number(card_number: str) -> str:
    """Функиця, которая маскрирует номер карты по примеру: XXXX XX** **** XXXX"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Неправильный номер счета")
    start_num = card_number[:6]
    stars_num = "*" * 6
    end_num = card_number[-4:]
    masked_num = start_num + stars_num + end_num
    return " ".join(masked_num[i : i + 4] for i in range(0, len(masked_num), 4))


def get_mask_account(account_number: str) -> str:
    """Функиця, которая маскрирует номер счета по примеру: **XXXX"""
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Неправильный номер счета")
    masked_account = account_number[-4:]
    return "**" + masked_account
