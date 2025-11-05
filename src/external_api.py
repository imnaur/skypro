import os

import requests
from dotenv import load_dotenv

from .utils import read_json

# Загрузка токена из файла .env
load_dotenv()
api_key = os.getenv("API_KEY")


def currency_transactions(transaction: dict) -> float:
    "Функция принимает транзакции и возвращает сумму в рублях."
    if transaction is None:
        print("Пропущена транзакция! Не полная информация!", transaction)
        return 0.0

    currency = transaction["currency"]["code"]

    amount = transaction["amount"]
    if currency == "RUB":
        return float(amount)

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    print("Ответ API:", data)

    if "result" not in data:
        print("Ошибка в ответе API", data)
        return 0.0
    return float(data["result"])


result_list = [currency_transactions(t) for t in read_json()]
print(result_list)
