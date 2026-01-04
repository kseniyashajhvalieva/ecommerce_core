class Category:
    """Класс категории товаров."""
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров в категории
        """
        self.name: str = name
        self.description: str = description
        self.products: list = products

        Category.category_count += 1
        Category.product_count += len(products)
