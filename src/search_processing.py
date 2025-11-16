import re
from collections import Counter


def search_process(operations_list: list[dict], search: str) -> list[dict]:
    """
    Функция принимает данные о банковских операциях и строку поиска,
     а затем
    возвращает соответствующие транзакции.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    new_operations_list = [o for o in operations_list if "description" in o and pattern.search(o["description"])]
    return new_operations_list


def operations_process(transactions_list: list[dict], categories: list) -> dict:
    """
    Функция принимает данные о банковских операциях и категории,
    возвращает словарь, где ключи - название категории,
     значение - количество операций в этой категории.
    """
    result = {category: 0 for category in categories}
    patterns = {category: re.compile(re.escape(category), re.IGNORECASE) for category in categories}
    for transaction in transactions_list:
        description = transaction.get("description", "")
        for category, pattern in patterns.items():
            if pattern.search(description):
                result[category] += 1
    counted = Counter(result)
    return counted
