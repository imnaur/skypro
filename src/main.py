def main():
    """Главная функция, отвечающая за основную логику виджета."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню: \n")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    client_answer = input("Введите номер пункта меню: ").strip()
    if client_answer == "1":
        print("Для обработки выбран JSON-файл.")
    elif client_answer == "2":
        print("Для обработки выбран CSV-файл.")
    elif client_answer == "3":
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный пункт меню. Программа завершена.")
        return

    valid_status = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        filter_answer = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )
        if filter_answer in valid_status:
            print(f'Операции отфильтрованы по статусу "{filter_answer}".\n')
            break
        else:
            print('Статус операции "{filter_answer}" недоступен.\n')

    sort_answer = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_answer == "да":
        print("Сортировка по дате применена.")
    else:
        pass
    order_answer = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
    if order_answer == "да":
        print("Отсортировано.")
    else:
        pass
    rub_only = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if rub_only == "да":
        print("Будут показаны только рублевые транзакции.")
    else:
        pass
    word_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if word_filter == "да":
        print(f"Применяется фильтр со словом: {word_filter}\n")
    else:
        pass

    print(" Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке:")


# После дополнительной информации будет завершена логика
# if not transactions:
# print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
