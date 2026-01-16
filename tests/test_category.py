from src.category import Category
from src.product import Product


def test_category_initialization() -> None:
    """Проверка создания категории"""
    p = Product("Телефон", "Смартфон", 50000.0, 10)
    cat = Category("Электроника", "Техника", [p])
    assert cat.name == "Электроника"
    assert cat.description == "Техника"
    assert "Телефон" in cat.products


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


def test_add_product() -> None:
    """Проверяет корректность добавления товара в категорию."""
    category = Category("Тест", "Описание", [])
    product = Product("Товар", "Описание", 100.0, 5)
    category.add_product(product)
    assert "Товар, 100.0 руб. Остаток: 5 шт." in category.products


def test_products_getter_format() -> None:
    """Проверяет формат вывода геттера products."""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Тест", "Описание", [product])
    expected = "Товар, 100.0 руб. Остаток: 5 шт.\n"
    assert category.products == expected


def test_category_str() -> None:
    """Проверяет строковое представление категории."""
    p1 = Product("Товар1", "Описание", 100.0, 2)
    p2 = Product("Товар2", "Описание", 200.0, 3)
    category = Category("Категория", "Описание", [p1, p2])
    assert str(category) == "Категория, количество продуктов: 5 шт."


def test_middle_price_with_products():
    """Проверка среднего ценника для категории с товарами"""
    p1 = Product("Товар1", "Описание1", 100.0, 2)
    p2 = Product("Товар2", "Описание2", 200.0, 3)
    category = Category("Тест", "Описание", [p1, p2])
    # Ожидаемый результат: (100 + 200) / 2 = 150.0
    assert category.middle_price() == 150.0
