from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Абстрактный метод инициализации продукта."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Абстрактный метод сложения продуктов."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактное свойство цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Абстрактный сеттер цены."""
        pass

    @property
    @abstractmethod
    def quantity(self) -> int:
        """Абстрактное свойство количества."""
        pass

    @quantity.setter
    @abstractmethod
    def quantity(self, value: int) -> None:
        """Абстрактный сеттер количества."""
        pass
