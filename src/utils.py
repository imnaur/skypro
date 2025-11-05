import json

import requests

url = "https://drive.google.com/uc?export=download&id=1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy"
response = requests.get(url)

data = response.json()
# Сохраняем JSON локально при помощи ссылки к файлу
save_path = "/Users/imnaur/PycharmProjects/Skypro/data/operations.json"
with open(save_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


# Читаем локально сохраненный JSON
def read_json():
    """Функция читает локально сохраненный файл JSON."""
    with open(save_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not data:
        print("No transactions found")
        return []
    new_transactions_list = []
    for transaction in data:
        if not transaction.get("operationAmount"):
            continue
        new_transactions_list.append(transaction["operationAmount"])
    return new_transactions_list


res = read_json()
print(res)
