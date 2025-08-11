from typing import List, Set

from src.models.product import Product


class Category:
    """
    Класс для представления категории товаров в магазине.
    """

    total_categories: int = 0
    total_unique_products: int = 0
    _existing_products: Set[int] = set()

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """
        Инициализирует экземпляр класса Category.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов категории
        """
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []

        Category.total_categories += 1

        # Добавляем только новые уникальные продукты
        for product in self.__products:
            self._add_to_unique_products(product)

    @classmethod
    def reset_counters(cls):
        """Сброс счётчиков для тестирования"""
        cls.total_categories = 0
        cls.total_unique_products = 0
        cls._existing_products = set()

    @classmethod
    def _add_to_unique_products(cls, product: Product):
        """Внутренний метод для добавления продукта в уникальные"""
        if id(product) not in cls._existing_products:
            cls._existing_products.add(id(product))
            cls.total_unique_products += 1

    @property
    def products(self) -> str:
        """Возвращает список продуктов категории."""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self) -> int:
        return len(self.__products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )

        self._add_to_unique_products(product)
        self.__products.append(product)

    @property
    def average_price(self) -> float:
        """Рассчитывает среднюю цену продуктов в категории."""
        try:
            return sum(p.price for p in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    @property
    def products_list(self) -> List[Product]:
        """Альтернативный геттер для получения списка продуктов"""
        return self.__products
