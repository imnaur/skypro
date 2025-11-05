import pytest

from src.decorators import log


def test_log(capsys):
    @log()
    def add(a, b):
        return a + b

    add(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(4, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (4, 0), {}\n" in captured.out
