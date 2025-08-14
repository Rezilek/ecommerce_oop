import json
from pathlib import Path
from typing import List

from src.models.category import Category
from src.models.product import Product


def load_categories_from_json(file_path: str) -> List[Category]:
    """
    Загружает данные о категориях и продуктах из JSON файла.

    :param file_path: Путь к JSON файлу
    :return: Список объектов Category
    :raises FileNotFoundError: Если файл не найден
    :raises json.JSONDecodeError: Если файл содержит некорректный JSON
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Ошибка декодирования JSON", doc=file_path, pos=0)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=float(product_data["price"]),
                quantity=int(product_data["quantity"]),
            )
            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories


def get_json_path(relative_path: str) -> str:
    """
    Возвращает абсолютный путь к JSON файлу относительно корня проекта.

    :param relative_path: Относительный путь к файлу
    :return: Абсолютный путь к файлу
    """
    return str(Path(__file__).parent.parent.parent / relative_path)
