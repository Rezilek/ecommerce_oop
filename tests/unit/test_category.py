import pytest

from src.models.category import Category
from src.models.product import Product


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        Category.reset_counters()
        yield
        Category.reset_counters()

    @pytest.fixture
    def sample_product(self):
        return Product("Телевизор", "Ультра HD 4K", 50000.0, 10)

    @pytest.fixture
    def sample_category(self, sample_product):
        return Category("Электроника", "Техника для дома", [sample_product])

    def test_category_initialization(self, sample_category):
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Техника для дома"
        assert len(sample_category.products_list) == 1

    def test_category_str(self, sample_category):
        assert str(sample_category) == "Электроника, количество продуктов: 1 шт."

    def test_category_len(self, sample_category):
        assert len(sample_category) == 1

    def test_add_product(self, sample_category):
        initial_count = len(sample_category.products_list)
        new_product = Product("Ноутбук", "Игровой", 80000.0, 5)
        sample_category.add_product(new_product)
        assert len(sample_category.products_list) == initial_count + 1
        assert sample_category.products_list[-1] == new_product

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
        test_category = Category("Тест", "Тест", [])
        assert Category.total_categories == initial_count + 1

    def test_unique_products_count(self):
        # Проверяем начальное состояние
        assert Category.total_unique_products == 0

        # Первый продукт
        product1 = Product("Test", "Desc", 100, 1)
        category1 = Category("Test1", "Test1", [product1])
        assert Category.total_unique_products == 1

        # Тот же продукт (должен игнорироваться для уникального счётчика)
        product_same = Product("Test", "Desc", 100, 1)  # Новый объект с теми же данными
        category2 = Category("Test2", "Test2", [product_same])
        assert (
            Category.total_unique_products == 2
        )  # Теперь 2, так как это другой объект

    def test_private_products(self):
        category = Category("Test", "Desc", [])
        with pytest.raises(AttributeError):
            _ = category.__products

    def test_products_property(self):
        p1 = Product("P1", "Desc", 100, 1)
        p2 = Product("P2", "Desc", 200, 2)
        category = Category("Test", "Desc", [p1, p2])

        products_str = category.products
        assert "P1, 100.0 руб. Остаток: 1 шт." in products_str
        assert "P2, 200.0 руб. Остаток: 2 шт." in products_str
