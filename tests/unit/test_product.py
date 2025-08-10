import pytest
from src.models.product import Product


class TestProduct:
    @pytest.fixture
    def sample_product(self):
        return Product("Телевизор", "Ультра HD 4K", 50000.0, 10)

    def test_product_initialization(self, sample_product):
        assert sample_product.name == "Телевизор"
        assert sample_product.description == "Ультра HD 4K"
        assert sample_product.price == 50000.0
        assert sample_product.quantity == 10

    def test_product_str(self, sample_product):
        assert str(sample_product) == "Телевизор, 50000.0 руб. Остаток: 10 шт."

    def test_product_repr(self, sample_product):
        assert repr(sample_product) == "Product(name='Телевизор', description='Ультра HD 4K', price=50000.0, quantity=10)"

    @pytest.mark.parametrize("price,quantity", [
        (-100, 5),
        (100, -5),
        (0, 0),
        (1e6, 1e6)
    ])
    def test_product_edge_cases(self, price, quantity):
        product = Product("Test", "Test", price, quantity)
        assert product.price == price
        assert product.quantity == quantity
