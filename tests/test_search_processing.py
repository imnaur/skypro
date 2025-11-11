from src.search_processing import operations_process, search_process


def test_search_process():
    """Тест проверяет работоспособность функции искать и фильтровать транзакции по поисковым данным."""
    transactions = [
        {"description": "Оплата продуктов в магазине", "amount": 900},
        {"description": "Такси до работы", "amount": 500},
        {"description": "Оплата продуктов онлайн", "amount": 700},
        {"description": "Кафе и ресторан", "amount": 2000},
        {"description": "Такси домой", "amount": 250},
    ]
    search_word = "такси"
    search_result = search_process(transactions, search_word)
    print(search_result)


def test_operations_process():
    """Тест проверяет работоспособность функции разделать транзакции на категории."""
    transactions = [
        {"description": "Оплата продуктов в магазине"},
        {"description": "Такси до работы"},
        {"description": "Оплата продуктов онлайн"},
        {"description": "Кафе и ресторан"},
        {"description": "Такси домой"},
    ]
    categories = ["продукт", "такси", "кафе"]
    result = operations_process(transactions, categories)
    print(result)
