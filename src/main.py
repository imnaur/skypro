import json
import os

import pandas as pd


def main():
    """Главная функция, отвечающая за основную логику виджета."""

    def mask_number(number: str) -> str:
        """Маскирует номер карты или счета."""
        if "Счет" in number:
            return "Счет **" + number[-4:]
        else:
            digits = [c for c in number if c.isdigit()]
            if len(digits) >= 16:
                return number[: len(number) - 10] + "** **** " + "".join(digits[-4:])
            return number

    def format_transaction(row):
        """Функция выводит заданный по ТЗ формат ответов."""
        data_str = row.get("date", "")
        try:
            date_formated = pd.to_datetime(data_str).strftime("%d.%m.%Y")
        except ValueError:
            date_formated = data_str

        from_acc = mask_number(str(row.get("from", ""))) if pd.notnull(row.get("from", "")) else ""
        to_acc = mask_number(str(row.get("to", ""))) if pd.notnull(row.get("to", "")) else ""

        s = f"{date_formated} {row.get("description", "")}\n"
        if from_acc and to_acc:
            s += f"{from_acc} -> {to_acc}\n"
        elif from_acc:
            s += f"{from_acc}\n"
        elif to_acc:
            s += f"{to_acc}\n"
        s += f"Сумма: {row.get("amount", "")} {row.get("currency_code", "")}\n"
        return s

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
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            df = pd.json_normalize(data)
        except FileNotFoundError:
            print("Файл не найден.")
            return

    elif client_answer == "2":
        file_path = os.path.join(DATA_DIR, "transactions.csv")
        print("Для обработки выбран CSV-файл.")
        try:
            df = pd.read_csv(file_path, sep=";")
        except FileNotFoundError:
            print("Файл не найден.")
            return

    elif client_answer == "3":
        file_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
        try:
            df = pd.read_excel(file_path, engine="openpyxl")
        except Exception:
            print("Файл не настоящий Excel, читаем как CSV.")
            df = pd.read_csv(file_path, sep=";")

    else:
        print("Неверный пункт меню. Программа завершена.")
        return

    status_col = "state"
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
            df = df[df[status_col] == filter_answer]
            print(f'Операции отфильтрованы по статусу "{filter_answer}".\n')
            break
        else:
            print(f'Статус операции "{filter_answer}" недоступен.\n')
    if "date" in df.columns:
        order_answer = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if order_answer == "да":
            order_type = input("По возрастанию или убыванию?\n").strip().lower()
            ascending = True if order_type == "возрастанию" else False
            df = df.sort_values(by="date", ascending=ascending)
            print("Отсортировано.")
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
            df = df[df["description"].str.lower().str.contains(keyword)]
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
