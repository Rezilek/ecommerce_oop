def validate_price(value):
    """Валидация цены продукта с подробными сообщениями об ошибках"""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Цена должна быть числом, получено {type(value)}")
    if value <= 0:
        raise ValueError(f"Цена должна быть положительной, получено {value}")
    return float(value)
