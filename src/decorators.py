from functools import wraps


def log(filename=None):
    """
    Декоратор log. Логирует начало и конец выполнения функции, а также её результат или ошибку.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message)
                raise
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(message)
            else:
                print(message)
            return func(*args, **kwargs)

        return wrapper

    return decorator
