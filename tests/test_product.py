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
