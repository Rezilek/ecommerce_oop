from src.models.product import Product, Smartphone


if __name__ == '__main__':
    # При создании объектов будет выводиться информация о создании
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    # Тестирование миксина
    print(repr(product1))

    # Тестирование наследования
    smartphone = Smartphone("Test Phone", "Desc", 1000, 2, 95.5, "S23", 256, "Black")
    print(isinstance(smartphone, Product))
