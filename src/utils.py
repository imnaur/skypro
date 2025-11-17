import json
import logging
import os

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


# Читаем локально сохраненный JSON
def read_json(save_path):
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

    new_transactions_list = []
    for transaction in data:
        if not transaction.get("operationAmount"):
            json_logger.warning("Пропущен файл - недостаточно информации!")
            continue
        new_transactions_list.append(transaction)
    json_logger.info("Конец процесса чтения JSON файла")
    return new_transactions_list


if __name__ == "__main__":
    save_path = "/Users/imnaur/PycharmProjects/Skypro/data/operations.json"
    res = read_json(save_path)
    print(res)
