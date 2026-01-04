class Product:
    """Класс товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация товара.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара в наличии
        """
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity
