import io
import sys
from src.product import Product


def test_print_mixin_output():
    """Проверка вывода миксина при создании объекта."""
    captured_output = io.StringIO()
    sys.stdout = captured_output

    Product("Test", "Description", 100.0, 5)

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "Product('Test', 'Description', 100.0, 5)" in output
