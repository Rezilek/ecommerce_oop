from abc import ABC

import pytest

from src.models.base import BaseProduct
from src.models.product import Product, Smartphone


def test_base_product_is_abstract():
    """Тест, что BaseProduct является абстрактным классом."""
    assert issubclass(BaseProduct, ABC)

    # Попытка создать экземпляр абстрактного класса должна вызвать ошибку
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100, 1)


def test_product_inherits_from_base_product():
    """Тест, что Product наследуется от BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_logging_mixin_functionality():
    """Тест функциональности миксина логирования."""
    # При создании объекта должен выводиться лог
    product = Product("Test", "Description", 100, 5)
    assert hasattr(product, "__repr__")

    # Проверяем repr
    repr_str = repr(product)
    assert "Product" in repr_str
    assert "name='Test'" in repr_str


def test_smartphone_inheritance_chain():
    """Тест цепочки наследования Smartphone."""
    phone = Smartphone("Phone", "Desc", 1000, 2, 90, "X", 128, "Black")
    assert isinstance(phone, Product)
    assert isinstance(phone, BaseProduct)
