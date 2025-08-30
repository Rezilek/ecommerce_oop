def validate_price(value: float) -> float:
    """Проверяет и нормализует цену товара.

    Args:
        value: Проверяемое значение цены

    Returns:
        float: Нормализованная цена

    Raises:
        ValueError: Если цена <= 0
        TypeError: Если цена не числовая
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Цена должна быть числом")
    if value <= 0:
        raise ValueError("Цена должна быть положительной")
    return float(value)


def validate_quantity(value: int) -> int:
    """Проверяет и нормализует количество товара.

    Args:
        value: Проверяемое значение количества

    Returns:
        int: Нормализованное количество

    Raises:
        ValueError: Если количество = 0 или отрицательное
        TypeError: Если количество не целое число
    """
    if not isinstance(value, int):
        raise TypeError("Количество должно быть целым числом")
    if value == 0:
        raise ValueError("Товар с нулевым количеством не может быть добавлен")
    if value < 0:
        raise ValueError("Количество не может быть отрицательным")
    if value > 1_000_000:
        raise ValueError("Слишком большое количество (максимум 1_000_000)")
    return value
