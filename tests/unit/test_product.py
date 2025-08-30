from contextlib import nullcontext as does_not_raise

import pytest

from src.models.product import LawnGrass, Product, Smartphone
from src.utils.validators import validate_quantity


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


def test_smartphone_initialization():
    """Тест инициализации смартфона."""
    phone = Smartphone("iPhone", "Смартфон", 100000, 5, 95.5, "15 Pro", 512, "Black")
    assert phone.name == "iPhone"
    assert phone.efficiency == 95.5
    assert phone.model == "15 Pro"
    assert phone.memory == 512
    assert phone.color == "Black"


def test_lawn_grass_initialization():
    """Тест инициализации газонной травы."""
    grass = LawnGrass(
        "Трава", "Газонная трава", 500, 10, "Россия", "14 дней", "Зеленая"
    )
    assert grass.name == "Трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "Зеленая"


def test_add_same_class_products():
    """Тест сложения товаров одного класса."""
    phone1 = Smartphone("Phone1", "Desc", 1000, 2, 90, "X", 128, "Black")
    phone2 = Smartphone("Phone2", "Desc", 2000, 3, 95, "Y", 256, "White")
    assert phone1 + phone2 == 1000 * 2 + 2000 * 3

    grass1 = LawnGrass("Grass1", "Desc", 500, 5, "RU", "10d", "Green")
    grass2 = LawnGrass("Grass2", "Desc", 700, 3, "US", "7d", "Blue")
    assert grass1 + grass2 == 500 * 5 + 700 * 3


def test_add_different_class_products():
    """Тест попытки сложения товаров разных классов."""
    phone = Smartphone("Phone", "Desc", 1000, 2, 90, "X", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 500, 5, "RU", "10d", "Green")

    with pytest.raises(TypeError):
        phone + grass

    with pytest.raises(TypeError):
        grass + phone


def test_product_with_zero_quantity():
    """Тест создания товара с нулевым количеством."""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Test", "Description", 100.0, 0)


def test_validate_quantity_zero():
    """Тест валидации нулевого количества."""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        validate_quantity(0)


def test_validate_quantity_negative():
    """Тест валидации отрицательного количества."""
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        validate_quantity(-5)


def test_validate_quantity_valid():
    """Тест валидации корректного количества."""
    assert validate_quantity(1) == 1
    assert validate_quantity(100) == 100
