from src.lawn_grass import LawnGrass


def test_lawn_grass_creation() -> None:
    """Проверка создания объекта LawnGrass."""
    grass = LawnGrass("Трава", "Мягкая", 500.0, 10, "Россия", "7 дней", "Зелёный")
    assert grass.name == "Трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"


def test_lawn_grass_add_same_type() -> None:
    """Проверка сложения двух объектов LawnGrass."""
    grass1 = LawnGrass("Трава1", "Описание", 300.0, 5, "РФ", "5 дней", "Тёмный")
    grass2 = LawnGrass("Трава2", "Описание", 400.0, 3, "США", "10 дней", "Светлый")
    assert grass1 + grass2 == 300.0 * 5 + 400.0 * 3
