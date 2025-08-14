from contextlib import nullcontext as does_not_raise

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

    def test_product_str(self, sample_product):
        assert str(sample_product) == "Телевизор, 50000.0 руб. Остаток: 10 шт."

    def test_product_repr(self, sample_product):
        assert (
            repr(sample_product)
            == "Product(name='Телевизор', description='Ультра HD 4K', price=50000.0, quantity=10)"
        )

    @pytest.mark.parametrize(
        "price,quantity,expectation",
        [
            (-100, 5, pytest.raises(ValueError)),
            (100, -5, does_not_raise()),
            (0, 0, pytest.raises(ValueError)),
            (1000000, 1000000, does_not_raise()),
        ],
    )
    def test_product_edge_cases(self, price, quantity, expectation):
        with expectation:
            product = Product("Test", "Test", price, quantity)
            if isinstance(expectation, does_not_raise):
                assert product.price == float(price)

    def test_price_property(self):
        product = Product("Test", "Desc", 100, 1)
        assert product.price == 100.0

        with pytest.raises(ValueError):
            product.price = -50

        product.price = 150
        assert product.price == 150.0
