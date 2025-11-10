import os

import pandas as pd
import requests

# CSV FILE
# Скачивание CSV файла с URL
url = "https://raw.githubusercontent.com/skypro-008/transactions/refs/heads/main/transactions.csv"
response = requests.get(url)

# Сохраняем CSV файл локально при помощи ссылки к файлу
save_path = "/Users/imnaur/PycharmProjects/Skypro/data/transactions.csv"
os.makedirs(os.path.dirname(save_path), exist_ok=True)
with open(save_path, "wb") as file:
    file.write(response.content)


def reading_csv(save_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV"""
    df_csv = pd.read_csv(save_path, sep=";")
    df_csv_list = df_csv.to_dict(orient="records")
    return df_csv_list


csv_result = reading_csv(save_path)
print(csv_result[:3])

# EXCEL FILE
# Скачивание EXCEL файла с URL, сохраняется в загрузках
# Путь к файлу в загрузках
file_path = "/Users/imnaur/Downloads/transactions_excel.xlsx"


def reading_excel(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel"""
    df = pd.read_excel(file_path, engine="openpyxl")
    df_list = df.to_dict(orient="records")
    return df_list


#excel_result = reading_excel(file_path)
# print(excel_result[:3])
