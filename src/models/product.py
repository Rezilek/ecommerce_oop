from typing import Any

from src.models.base import BaseProduct
from src.models.logging_mixin import LoggingMixin
from src.utils.validators import validate_price, validate_quantity


class Product(LoggingMixin, BaseProduct):
    """Класс для представления товара в магазине.

    Наследуется от BaseProduct и LoggingMixin.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара (должна быть положительной)
        quantity (int): Количество товара (не может быть отрицательным)
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализирует экземпляр класса Product.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара

        Raises:
            ValueError: Если цена или количество недопустимые
        """
        self.name = name
        self.description = description
        self.__price = validate_price(price)
        self.__quantity = validate_quantity(quantity)
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Возвращает цену товара.

        Returns:
            float: Цена товара
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Устанавливает цену товара с проверкой.

        Args:
            value: Новая цена товара

        Raises:
            ValueError: Если цена недопустимая
        """
        self.__price = validate_price(value)

    @property
    def quantity(self) -> int:
        """Возвращает количество товара.

        Returns:
            int: Количество товара
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """Устанавливает количество товара с проверкой.

        Args:
            value: Новое количество товара

        Raises:
            ValueError: Если количество недопустимое
        """
        self.__quantity = validate_quantity(value)

    def __str__(self) -> str:
        """Возвращает строковое представление товара.

        Returns:
            str: Строка в формате "Название, цена руб. Остаток: количество шт."
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Складывает товары (сумма цен * количества).

        Args:
            other: Другой товар для сложения

        Returns:
            float: Общая стоимость товаров

        Raises:
            TypeError: Если other не является Product или классы товаров разные
        """
        if not isinstance(other, type(self)):
            raise TypeError("Можно складывать только товары одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для представления смартфона в магазине (наследуется от Product)."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует экземпляр класса Smartphone."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы в магазине (наследуется от Product)."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует экземпляр класса LawnGrass."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
