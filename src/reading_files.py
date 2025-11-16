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


def reading_csv(save_path: str, sep=";") -> list[dict]:
    """Функция для считывания финансовых операций из CSV"""
    df_csv = pd.read_csv(save_path, sep=sep)
    df_csv_list = df_csv.to_dict(orient="records")
    return df_csv_list


#EXCEL FILE
url_excel = "https://raw.githubusercontent.com/skypro-008/transactions/refs/heads/main/transactions_excel.xlsx"
save_path = "/Users/imnaur/PycharmProjects/Skypro/data/transactions_excel.xlsx"
os.makedirs(os.path.dirname(save_path), exist_ok=True)
r = requests.get(url_excel)
with open(save_path, "wb") as f:
    f.write(r.content)


def reading_excel(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel"""
    df = pd.read_excel(file_path, engine="openpyxl")
    return df.to_dict(orient="records")




