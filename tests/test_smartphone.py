from src.smartphone import Smartphone


def test_smartphone_creation() -> None:
    """Проверка создания объекта Smartphone."""
    phone = Smartphone("Test", "Desc", 100.0, 5, 95.5, "Model", 128, "Black")
    assert phone.name == "Test"
    assert phone.efficiency == 95.5


def test_smartphone_add_same_type() -> None:
    """Проверка сложения двух смартфонов."""
    phone1 = Smartphone("Phone1", "Desc", 100.0, 2, 90.0, "M1", 64, "White")
    phone2 = Smartphone("Phone2", "Desc", 200.0, 3, 95.0, "M2", 128, "Black")
    assert phone1 + phone2 == 100.0 * 2 + 200.0 * 3
