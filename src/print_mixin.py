class PrintMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__}{args}")
