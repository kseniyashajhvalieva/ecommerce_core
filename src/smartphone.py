from src.product import Product


class Smartphone(Product):
    """Класс Смартфон, наследник Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency: float = efficiency
        self.model: str = model
        self.memory: int = memory
        self.color: str = color
