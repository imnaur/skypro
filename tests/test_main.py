from unittest.mock import patch
from src.main import main


def test_main_runs():
    """Тест проверяет главную функцию на работоспособность."""
    # Подготовим последовательность ответов пользователя для input()
    user_inputs = ["1", "EXECUTED", "нет", "нет", "нет"]

    with patch("builtins.input", side_effect=user_inputs):
        main()
