def filter_by_state(list_of_state : list[dict], state='EXECUTED') -> list[dict]:
    """"""
    new_state_list = []
    for state in list_of_state:
        for key, value in state.items():
            if value == 'EXECUTED':
                new_state_list.append(state)
    return new_state_list


