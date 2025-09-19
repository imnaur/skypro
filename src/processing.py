def filter_by_state(list_of_state: list[dict], state="EXECUTED") -> list[dict]:
    """Функция, которая фильтрует словари по состоянию."""
    new_state_list = []
    for state in list_of_state:
        for key, value in state.items():
            if value == "EXECUTED":
                new_state_list.append(state)
    return new_state_list


def sort_by_date(data: list[dict]) -> list[dict]:
    """Функиця, которая сортирует список по порядку убывания."""
    sorted_date = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_date
