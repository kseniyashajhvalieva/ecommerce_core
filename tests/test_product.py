from src.product import Product


def test_product_initialization() -> None:
    """Проверка создания товара"""
    p = Product("Телефон", "Смартфон", 50000.0, 10)
    assert p.name == "Телефон"
    assert p.description == "Смартфон"
    assert p.price == 50000.0
    assert p.quantity == 10


def test_product_attributes() -> None:
    """Проверка типов данных атрибутов"""
    p = Product("Книга", "Художественная", 500.0, 5)
    assert isinstance(p.name, str)
    assert isinstance(p.price, float)
    assert isinstance(p.quantity, int)


def test_new_product() -> None:
    """Проверяет создание товара через класс-метод new_product."""
    data = {"name": "Тест", "description": "Описание", "price": 100.0, "quantity": 5}
    product = Product.new_product(data)
    assert product.name == "Тест"
    assert product.price == 100.0
    assert product.quantity == 5


def test_price_setter_positive() -> None:
    """Проверяет корректное обновление цены через сеттер."""
    product = Product("Тест", "Описание", 100.0, 5)
    product.price = 200.0
    assert product.price == 200.0


def test_price_setter_negative() -> None:
    """Проверяет, что сеттер игнорирует неположительную цену."""
    product = Product("Тест", "Описание", 100.0, 5)
    product.price = -50.0
    assert product.price == 100.0  # Цена не должна измениться
