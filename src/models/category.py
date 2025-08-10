from typing import List
from src.models.product import Product


class Category:
    """
    Класс для представления категории товаров в магазине.
    """
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализирует экземпляр класса Category.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов категории
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_unique_products += len(set(products))

    @property
    def products(self):
        """Возвращает список продуктов категории."""
        return self.__products

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        return len(self.__products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.total_unique_products += 1

    @property
    def average_price(self) -> float:
        """Рассчитывает среднюю цену продуктов в категории."""
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0.0
