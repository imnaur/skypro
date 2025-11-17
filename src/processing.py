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

    # from/to
    from_acc = str(row.get("from", ""))
    to_acc = str(row.get("to", ""))

    if from_acc:
        digits = "".join(filter(str.isdigit, from_acc))
        if len(digits) >= 16:
            from_acc = from_acc.replace(digits, mask_account_card(digits))
    if to_acc:
        digits = "".join(filter(str.isdigit, to_acc))
        if len(digits) >= 20:
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
