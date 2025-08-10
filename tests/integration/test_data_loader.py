import pytest
import json

from src.models.data_loader import load_categories_from_json, get_json_path
from src.models.category import Category
from src.models.product import Product


class TestDataLoader:
    @pytest.fixture
    def valid_json_path(self):
        return get_json_path("data/products.json")

    @pytest.fixture
    def invalid_json_path(self):
        return "nonexistent_file.json"

    @pytest.fixture
    def malformed_json_path(self, tmp_path):
        path = tmp_path / "malformed.json"
        path.write_text("{invalid json}")
        return str(path)

    def test_load_valid_json(self, valid_json_path):
        categories = load_categories_from_json(valid_json_path)
        assert isinstance(categories, list)
        assert all(isinstance(cat, Category) for cat in categories)
        assert len(categories) > 0
        assert all(len(cat.products) > 0 for cat in categories)
        assert all(isinstance(p, Product) for cat in categories for p in cat.products)

    def test_load_nonexistent_file(self, invalid_json_path):
        with pytest.raises(FileNotFoundError):
            load_categories_from_json(invalid_json_path)

    def test_load_malformed_json(self, malformed_json_path):
        with pytest.raises(json.JSONDecodeError):
            load_categories_from_json(malformed_json_path)

    def test_json_structure(self, valid_json_path):
        with open(valid_json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        assert isinstance(data, list)
        for category in data:
            assert 'name' in category
            assert 'description' in category
            assert 'products' in category
            for product in category['products']:
                assert 'name' in product
                assert 'description' in product
                assert 'price' in product
                assert 'quantity' in product
