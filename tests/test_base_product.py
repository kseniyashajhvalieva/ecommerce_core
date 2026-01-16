import pytest  # type: ignore

from src.base_product import BaseProduct


def test_base_product_is_abstract():
    """Проверка, что BaseProduct нельзя инстанциировать."""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100.0, 5)
