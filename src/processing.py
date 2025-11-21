import pandas as pd
from src.widget import get_date, mask_account_card

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
    date_str = row.get("date", "")
    try:
        date_formatted = get_date(str(date_str))
    except ValueError:
        date_formatted = date_str

    # получаем значения
    from_acc = row.get("from")
    to_acc = row.get("to")

    # приводим к строке и очищаем
    from_acc = str(from_acc).strip() if from_acc else ""
    to_acc = str(to_acc).strip() if to_acc else ""

    # устраняем NaN / None
    if from_acc.lower() == "nan":
        from_acc = ""
    if to_acc.lower() == "nan":
        to_acc = ""

    # маскирование from_acc
    if from_acc:
        digits = "".join(ch for ch in from_acc if ch.isdigit())
        if len(digits) in (16, 20):
            from_acc = from_acc.replace(digits, mask_account_card(digits))

    # маскирование to_acc
    if to_acc:
        digits = "".join(ch for ch in to_acc if ch.isdigit())
        if len(digits) in (16, 20):
            to_acc = to_acc.replace(digits, mask_account_card(digits))

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
