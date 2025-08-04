# E-commerce OOP Core

Ядро интернет-магазина с реализацией основных сущностей на ООП.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-логин/ecommerce_oop.git
   cd ecommerce_oop
   ```

2. Установите зависимости:
   ```bash
   poetry install
   ```

## Использование

Основные модули:

- `product.py` - класс товара
- `category.py` - класс категории товаров
- `data_loader.py` - загрузка данных из JSON

Пример использования:

```python
from src.models import Product, Category, load_categories_from_json

# Создание объектов
product = Product("Телевизор", "4K UHD", 50000.0, 10)
category = Category("Электроника", "Техника", [product])

# Загрузка данных
categories = load_categories_from_json("data/products.json")
```

## Тестирование

```bash
# Запуск тестов
poetry run pytest

# Проверка покрытия
poetry run pytest --cov=src --cov-report=html

# Проверка стиля кода
poetry run flake8 src tests
poetry run mypy src tests
```

## Структура проекта

```
ecommerce_oop/
├── src/               # Исходный код
├── tests/             # Тесты
├── data/              # Данные
├── pyproject.toml     # Конфигурация Poetry
└── README.md          # Документация
```
````

Эта структура проекта обеспечивает:
- Четкое разделение на модули
- Полное покрытие тестами
- Возможность легкого расширения функционала
- Простоту использования и интеграции
