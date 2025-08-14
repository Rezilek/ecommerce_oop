from src.models.category import Category
from src.models.product import Product


class TestCategoryProductsIntegration:
    def test_add_product_to_category(self):
        category = Category("Electronics", "Tech")
        product = Product("Phone", "Smartphone", 1000, 5)

        category.add_product(product)
        assert "Phone, 1000.0 руб. Остаток: 5 шт." in category.products
