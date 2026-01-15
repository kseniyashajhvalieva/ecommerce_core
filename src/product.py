from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    """Класс товара."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """
        Инициализация товара.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара в наличии
        """
        PrintMixin.__init__(self, name, description, price, quantity)
        BaseProduct.__init__(self, name, description, price, quantity)
        self.name: str = name
        self.description: str = description
        self.__price: float = price
        self.quantity: int = quantity

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """Создает продукт из словаря."""
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=product_dict["price"],
            quantity=product_dict["quantity"],
        )

    @property
    def price(self) -> float:
        """Возвращает цену."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает цену, если она положительна."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return self.price * self.quantity + other.price * other.quantity
