from src.product import Product


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
        self.__products: list = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: 'Product') -> None:
        from src.product import Product
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников.")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку с товарами."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
