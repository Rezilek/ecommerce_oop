from ..utils.validators import validate_price


class Product:
    """
    Класс для представления продукта в магазине.
    """

    def __init__(self, name, description, price, quantity):
        """
        Инициализирует экземпляр класса Product.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.__price = validate_price(price)  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = validate_price(value)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity})"

    @classmethod
    def new_product(cls, product_data, existing_products=None):
        # Реализация создания нового продукта
        pass
