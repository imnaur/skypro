import json
import logging
import os

import requests

# Логер для функции read_json()
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_folder = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(log_folder, exist_ok=True)

LOG_FILE = os.path.join(log_folder, "utils.log")

# Создание логера
json_logger = logging.getLogger(__name__)
json_logger.setLevel(logging.DEBUG)

# Обработка файла
file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Формат сообщений
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление обработчика
json_logger.addHandler(file_handler)


# Скачивание JSON файла с URL
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
    json_logger.info("Начало процесса чтения JSON файла")

    try:
        with open(save_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        json_logger.error(f"Файл не найден: {save_path}")
        return []
    except json.decoder.JSONDecodeError:
        json_logger.error(f"Ошибка декодирования JSON в файле: {save_path}")
        return []
    if not data:
        json_logger.error("Файл пуст - нет транзакций!")
        return []

    with open(save_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not data:
        print("No transactions found")
        json_logger.warning("Ошибка чтения файла!")
        return []
    new_transactions_list = []
    for transaction in data:
        if not transaction.get("operationAmount"):
            json_logger.warning("Пропущен файл - недостаточно информации!")
            continue
        new_transactions_list.append(transaction["operationAmount"])
    json_logger.info("Конец процесса чтения JSON файла")
    return new_transactions_list


if __name__ == "__main__":
    res = read_json()
    print(res)
