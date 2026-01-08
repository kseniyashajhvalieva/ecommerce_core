from src.category import Category
from src.product import Product


def test_category_initialization() -> None:
    """Проверка создания категории"""
    p = Product("Телефон", "Смартфон", 50000.0, 10)
    cat = Category("Электроника", "Техника", [p])
    assert cat.name == "Электроника"
    assert cat.description == "Техника"
    assert len(cat.products) == 1


def test_category_counters() -> None:
    """Проверка счётчиков категорий и товаров"""
    initial_categories: int = Category.category_count
    initial_products: int = Category.product_count

    p1: Product = Product("Книга", "Художественная", 500.0, 5)
    p2: Product = Product("Тетрадь", "Школьная", 100.0, 20)

    cat: Category = Category("Канцелярия", "Офисные товары", [p1, p2])

    assert Category.category_count == initial_categories + 1
    assert Category.product_count == initial_products + 2
    assert cat.name == "Канцелярия"
