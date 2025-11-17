import os

import pandas as pd

from src.processing import filter_by_state, format_transaction, sort_by_date
from src.reading_files import reading_csv, reading_excel
from src.search_processing import search_process
from src.utils import read_json


def main():
    """Главная функция, отвечающая за основную логику виджета."""
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню: \n")
    print("Получить информацию о транзакциях из:\n1. JSON-файла\n2. CSV-файла\n3. XLSX-файла")

    client_answer = input("Введите номер пункта меню: ").strip()

    # Путь к файлам путем применения абсолютного пути
    BASE_DIR = os.path.dirname(__file__)
    PROJECT_DIR = os.path.dirname(BASE_DIR)
    DATA_DIR = os.path.join(PROJECT_DIR, "data")

    if client_answer == "1":
        file_path = os.path.join(DATA_DIR, "operations.json")
        print("Для обработки выбран JSON-файл.")
        dict_oper = read_json(file_path)
        df = pd.DataFrame(dict_oper)

    elif client_answer == "2":
        file_path = os.path.join(DATA_DIR, "transactions.csv")
        print("Для обработки выбран CSV-файл.")
        dict_oper = reading_csv(file_path)
        df = pd.DataFrame(dict_oper)

    elif client_answer == "3":
        file_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
        dict_oper = reading_excel(file_path)
        df = pd.DataFrame(dict_oper)

    else:
        print("Неверный пункт меню. Программа завершена.")
        return None

    while True:
        filter_answer = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )

        if filter_answer in ["EXECUTED", "CANCELED", "PENDING"]:
            df = pd.DataFrame(filter_by_state(df.to_dict(orient="records"), filter_answer))
            break
        else:
            print("Неверный статус. Попробуйте еще раз.")

    if isinstance(df, pd.DataFrame) and "date" in df.columns:
        order_answer = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if order_answer == "да":
            order_type = input("По возрастанию или убыванию?\n").strip().lower()
            reverse = order_type == "убыванию"
            df = pd.DataFrame(sort_by_date(df.to_dict(orient="records"), reverse=reverse))
    else:
        print("Нет столбца даты, пропущен фильтр.")

    currency_col = "currency_code" if "currency_code" in df.columns else None
    rub_only = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if rub_only == "да" and currency_col:
        df = df[df[currency_col] == "RUB"]
        print("Будут показаны только рублевые транзакции.")

    if "description" in df.columns:
        word_filter = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
        )
        if word_filter == "да":
            keyword = input("Введите слово для фильтрации: ")
            df = pd.DataFrame(search_process(df.to_dict(orient="records"), keyword))
            print(f"Применяется фильтр со словом: {keyword}\n")

    print(" Распечатываю итоговый список транзакций...")
    if df.empty:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(df)}\n")
        for _, row in df.iterrows():
            print(format_transaction(row))


if __name__ == "__main__":
    main()
