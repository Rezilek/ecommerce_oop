import pytest

from src.models.category import Category
from src.models.product import LawnGrass, Product, Smartphone


@pytest.fixture
def sample_product():
    return Product("Телевизор", "Ультра HD 4K", 50000.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Техника для дома", [sample_product])


def test_category_initialization(sample_category):
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома"
    assert len(sample_category.products_list) == 1


def test_category_str(sample_category):
    assert str(sample_category) == "Электроника, количество продуктов: 10 шт."


def test_category_len(sample_category):
    assert len(sample_category) == 1


def test_add_product(sample_category):
    initial_count = len(sample_category.products_list)
    new_product = Product("Ноутбук", "Игровой", 80000.0, 5)
    sample_category.add_product(new_product)
    assert len(sample_category.products_list) == initial_count + 1
    assert sample_category.products_list[-1] == new_product


def test_add_invalid_product(sample_category):
    with pytest.raises(TypeError):
        sample_category.add_product("invalid product")


def test_average_price(sample_category):
    assert sample_category.average_price == 50000.0
    sample_category.add_product(Product("Ноутбук", "Игровой", 80000.0, 5))
    assert sample_category.average_price == 65000.0


def test_empty_category_average_price():
    empty_category = Category("Пустая", "Пустая категория", [])
    assert empty_category.average_price == 0.0


def test_category_count():
    initial_count = Category.total_categories
    test_category = Category("Тест", "Тест", [])
    assert Category.total_categories == initial_count + 1


def test_unique_products_count():
    Category.reset_counters()
    product1 = Product("Test", "Desc", 100, 1)
    category1 = Category("Test1", "Test1", [product1])
    assert Category.total_unique_products == 1


def test_category_iterator(sample_category):
    products = [p for p in sample_category]
    assert len(products) == 1
    assert products[0].name == "Телевизор"


def test_add_inherited_products():
    """Тест добавления товаров-наследников в категорию."""
    category = Category("Test", "Test")

    phone = Smartphone("Phone", "Desc", 1000, 2, 90, "X", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 500, 5, "RU", "10d", "Green")

    category.add_product(phone)
    category.add_product(grass)

    assert len(category) == 2


def test_add_non_product_to_category():
    """Тест попытки добавления не-продукта в категорию."""
    category = Category("Test", "Test")

    with pytest.raises(TypeError):
        category.add_product("not a product")

    with pytest.raises(TypeError):
        category.add_product(123)
