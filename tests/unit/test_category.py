import pytest
from src.models.product import Product
from src.models.category import Category


class TestCategory:
    @pytest.fixture
    def sample_product(self):
        return Product("Телевизор", "Ультра HD 4K", 50000.0, 10)

    @pytest.fixture
    def sample_category(self, sample_product):
        return Category("Электроника", "Техника для дома", [sample_product])

    def test_category_initialization(self, sample_category, sample_product):
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Техника для дома"
        assert len(sample_category.products) == 1
        assert sample_category.products[0] == sample_product

    def test_category_str(self, sample_category):
        assert str(sample_category) == "Электроника, количество продуктов: 1 шт."

    def test_category_len(self, sample_category):
        assert len(sample_category) == 1

    def test_add_product(self, sample_category):
        initial_count = len(sample_category)
        new_product = Product("Ноутбук", "Игровой", 80000.0, 5)
        sample_category.add_product(new_product)
        assert len(sample_category) == initial_count + 1
        assert sample_category.products[-1] == new_product

    def test_add_invalid_product(self, sample_category):
        with pytest.raises(TypeError):
            sample_category.add_product("invalid product")

    def test_average_price(self, sample_category):
        assert sample_category.average_price == 50000.0
        sample_category.add_product(Product("Ноутбук", "Игровой", 80000.0, 5))
        assert sample_category.average_price == 65000.0

    def test_empty_category_average_price(self):
        empty_category = Category("Пустая", "Пустая категория", [])
        assert empty_category.average_price == 0.0

    def test_category_count(self):
        initial_count = Category.total_categories
        category = Category("Тест", "Тест", [])
        assert Category.total_categories == initial_count + 1

    def test_unique_products_count(self, sample_product):
        initial_count = Category.total_unique_products
        category = Category("Тест", "Тест", [sample_product, sample_product])
        assert Category.total_unique_products == initial_count + 1  # Только уникальные продукты
