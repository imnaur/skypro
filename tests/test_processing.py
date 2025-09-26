import pytest
from src.processing import filter_by_state, sort_by_date


#Проверка кода по статусу "state"
# проверяем EXECUTED
def test_filter_by_state_valid(list_of_states_1, list_of_states_2):
    result = filter_by_state(list_of_states_1, "EXECUTED")
    expected = [{'id': 1, 'state': 'EXECUTED'},
             {'id': 3, 'state': 'EXECUTED'}]
    assert result == expected

# проверяем CANCELED
    result = filter_by_state(list_of_states_2, "CANCELED")
    expected = [{'id': 4, 'state': 'CANCELED'},
             {'id': 6, 'state': 'CANCELED'}]
    assert result == expected



#Проверка через вывод ошибки ввода
@pytest.mark.parametrize("inp", [
    [],
[{'id': 1, 'state': ''}],
[{'id': 2, 'state': None}]
])
def test_filter_by_state_invalid(inp):
    with pytest.raises(ValueError):
        filter_by_state(inp, state="")




#Проверка кода по датам в порядке убывания или возрастания
def test_sort_by_date_valid(list_of_dates):
    expected = [
        {'id': 19, 'date': '2022-03-08T00:00:00'},
        {'id': 15, 'date': '2019-07-03T18:35:29.512364'},
        {'id': 17, 'date': '2018-07-05T18:35:29'},
]
    assert sort_by_date(list_of_dates) == expected