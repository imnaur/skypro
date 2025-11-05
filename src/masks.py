import logging
import os


# Логер для функции read_json()
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_folder = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(log_folder, exist_ok=True)

LOG_FILE = os.path.join(log_folder, "masks.log")

# Создание логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Обработка файла
file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Формат сообщений
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление обработчика
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты по примеру: XXXX XX** **** XXXX"""
    logger.info("Начало функции маскировки номеров карт")

    if len(card_number) != 16 or not card_number.isdigit():
        logger.error("Введен неправильный формат данных!")
        raise ValueError("Неправильный номер счета")
    start_num = card_number[:6]
    stars_num = "*" * 6
    end_num = card_number[-4:]
    masked_num = start_num + stars_num + end_num
    logger.info("Конец функции маскировки")
    return " ".join(masked_num[i : i + 4] for i in range(0, len(masked_num), 4))


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета по примеру: **XXXX"""
    logger.info("Начало функции маскировки номеров счетов")
    if len(account_number) != 20 or not account_number.isdigit():
        logger.error("Введен неправильный формат данных!")
        raise ValueError("Неправильный номер счета")
    masked_account = account_number[-4:]
    logger.info("Конец функции маскировки")
    return "**" + masked_account


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("12345678901234567890"))
