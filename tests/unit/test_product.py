import pytest
from contextlib import nullcontext as does_not_raise
from src.models.product import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта."""
    return Product("Телевизор", "Ультра HD 4K", 50000.0, 10)


def test_product_initialization(sample_product):
    """Тест инициализации продукта."""
    assert sample_product.name == "Телевизор"
    assert sample_product.description == "Ультра HD 4K"
    assert sample_product.price == 50000.0
    assert sample_product.quantity == 10


def test_product_str(sample_product):
    """Тест строкового представления продукта."""
    assert str(sample_product) == "Телевизор, 50000.0 руб. Остаток: 10 шт."


@pytest.mark.parametrize(
    "price,quantity,expectation",
    [
        (-100, 5, pytest.raises(ValueError, match="Цена должна быть положительной")),
        (
            100,
            -5,
            pytest.raises(ValueError, match="Количество не может быть отрицательным"),
        ),
        (0, 0, pytest.raises(ValueError, match="Цена должна быть положительной")),
        (100, 1_000_001, pytest.raises(ValueError, match="Слишком большое количество")),
        (1000000, 1000000, does_not_raise()),
    ],
    ids=[
        "negative_price",
        "negative_quantity",
        "zero_price",
        "too_large_quantity",
        "valid_values",
    ],
)
def test_product_edge_cases(price, quantity, expectation):
    """Тест граничных случаев при создании продукта."""
    with expectation:
        Product("Test", "Test", price, quantity)


def test_price_setter(sample_product):
    """Тест изменения цены через сеттер."""
    sample_product.price = 60000.0
    assert sample_product.price == 60000.0
    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        sample_product.price = -100


def test_quantity_setter(sample_product):
    """Тест изменения количества через сеттер."""
    sample_product.quantity = 15
    assert sample_product.quantity == 15
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        sample_product.quantity = -5


def test_product_add(sample_product):
    """Тест сложения продуктов."""
    other_product = Product("Ноутбук", "Игровой", 80000.0, 5)
    total = sample_product + other_product
    assert total == 50000.0 * 10 + 80000.0 * 5
