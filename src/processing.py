import pandas as pd
from src.widget import get_date
from src.masks import get_mask_card_number, get_mask_account

def filter_by_state(list_of_states: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая фильтрует список словарей по значению ключа 'state'."""
    if not state:
        raise ValueError("Отсутствует статус")
    new_states_list = []
    for item in list_of_states:
        if item.get("state") == state:
            new_states_list.append(item)
    return new_states_list


def sort_by_date(data: list[dict], reverse=False) -> list[dict]:
    """Функция, которая сортирует список словарей по ключу 'date'."""
    sorted_date = sorted(data, key=lambda x: x["date"], reverse=reverse)
    return sorted_date



def format_transaction(row):
    """Форматирует транзакцию для всех типов файлов (JSON, CSV, XLSX)."""

    # Дата
    data_str = row["date"] if "date" in row else ""
    try:
        date_formatted = get_date(str(data_str))
    except ValueError:
        date_formatted = data_str

    # from/to
    from_acc = ""
    if "from" in row and pd.notnull(row["from"]):
        from_number = "".join(filter(str.isdigit, str(row["from"])))
        if len(from_number) == 16:
            from_acc = get_mask_card_number(from_number)
        elif len(from_number) == 20:
            from_acc = get_mask_account(from_number)
        else:
            from_acc = row["from"]

    to_acc = ""
    if "to" in row and pd.notnull(row["to"]):
        to_number = "".join(filter(str.isdigit, str(row["to"])))
        if len(to_number) == 16:
            to_acc = get_mask_card_number(to_number)
        elif len(to_number) == 20:
            to_acc = get_mask_account(to_number)
        else:
            to_acc = row["to"]

    # Сумма и валюта
    amount = ""
    currency = ""
    if "operationAmount" in row:  # JSON
        amount_info = row["operationAmount"]
        amount = amount_info.get("amount", "")
        currency = amount_info.get("currency", {}).get("code", "")
    elif "amount" in row:  # CSV/XLSX
        amount = row["amount"]
        currency = row["currency_code"] if "currency_code" in row else ""

    # Формируем вывод
    s = f"{date_formatted} {row.get('description', '')}\n"
    if from_acc and to_acc:
        s += f"{from_acc} -> {to_acc}\n"
    elif from_acc:
        s += f"{from_acc}\n"
    elif to_acc:
        s += f"{to_acc}\n"
    s += f"Сумма: {amount} {currency}\n"

    return s