def filter_by_state(list_of_states: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая фильтрует список словарей по значению ключа 'state'."""
    new_states_list = []
    for item in list_of_states:
        if item.get("state") == state:
            new_states_list.append(item)
    return new_states_list


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Функиця, которая сортирует список словарей по ключу 'date'."""
    sorted_date = sorted(data, key=lambda x: x["date"], reverse=reverse)
    return sorted_date
