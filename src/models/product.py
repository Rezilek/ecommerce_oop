class Product:
    """
    Класс для представления продукта в магазине.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует экземпляр класса Product.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity})"
