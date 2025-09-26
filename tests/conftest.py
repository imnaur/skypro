import pytest


@pytest.fixture
def list_of_states_1() -> list[dict]:
    return [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "EXECUTED"}]


@pytest.fixture
def list_of_states_2() -> list[dict]:
    return [{"id": 4, "state": "CANCELED"}, {"id": 5, "state": "EXECUTED"}, {"id": 6, "state": "CANCELED"}]


@pytest.fixture
def list_of_dates() -> list[dict]:
    return [
        {"id": 15, "date": "2019-07-03T18:35:29.512364"},
        {"id": 17, "date": "2018-07-05T18:35:29"},
        {"id": 19, "date": "2022-03-08T00:00:00"},
    ]
