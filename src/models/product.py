from src.utils.validators import validate_price, validate_quantity


class Product:
    """Класс для представления товара в магазине.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара (должна быть положительной)
        quantity (int): Количество товара (не может быть отрицательным)
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
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

    @property
    def price(self) -> float:
        """Возвращает цену товара.

        Returns:
            float: Цена товара
        """
        return self.__price

    @price.setter
    def price(self, value: float):
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
    def quantity(self, value: int):
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

    def __add__(self, other: "Product") -> float:
        """Складывает товары (сумма цен * количества).

        Args:
            other: Другой товар для сложения

        Returns:
            float: Общая стоимость товаров

        Raises:
            TypeError: Если other не является Product
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return (self.price * self.quantity) + (other.price * other.quantity)
