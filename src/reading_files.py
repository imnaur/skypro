import os
from ctypes import c_double

import pandas as pd


def reading_csv(file_path: str, sep=";") -> list[dict]:
    """Функция для считывания финансовых операций из CSV"""
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден!")
        return []
    df_csv = pd.read_csv(file_path, sep=sep)
    return df_csv.to_dict(orient="records")



def reading_excel(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel"""
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден!")
        return []
    df = pd.read_excel(file_path, engine="openpyxl")
    return df.to_dict(orient="records")


if __name__ == "__main__":
    csv_path = "/Users/imnaur/PycharmProjects/Skypro/data/transactions.csv"
    excel_path = "/Users/imnaur/PycharmProjects/Skypro/data/transactions_excel.xls"

    csv_data = reading_csv(csv_path)
    excel_data = reading_excel(excel_path)

    print(csv_data)
    print(excel_data)



