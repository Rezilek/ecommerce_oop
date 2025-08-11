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

## Основные возможности

### Модели данных

- **Товары (Product)**:
  - Приватный атрибут цены с валидацией
  - Автоматическая конвертация цен в float
  - Защита от отрицательных цен
  - Класс-метод для создания из словаря

- **Категории (Category)**:
  - Приватный список товаров
  - Подсчет уникальных товаров
  - Расчет средней цены
  - Автоматическое ведение статистики

### Особенности реализации

- Полная типизация (mypy)
- Защищенные атрибуты
- Геттеры/сеттеры для контроля данных
- Поддержка JSON-импорта

## Использование

Основные модули:

- `product.py` - класс товара
- `category.py` - класс категории товаров
- `data_loader.py` - загрузка данных из JSON

Пример использования:

```python
from src.models import Product, Category

# Создание продукта
product = Product("Смартфон", "Android 13", 29999.0, 15)

# Установка цены с валидацией
try:
    product.price = -1000  # Вызовет ValueError
except ValueError as e:
    print(e)

# Создание категории
electronics = Category("Электроника", "Гаджеты и устройства")

# Добавление товара
electronics.add_product(product)

# Получение списка товаров
print(electronics.products)
```

## Тестирование

```bash
# Запуск тестов
poetry run pytest

# Проверка покрытия
poetry run pytest --cov=src --cov-report=html

# Проверка стиля кода
poetry run flake8 src tests

# Проверка типов
poetry run mypy src tests
```

## Структура проекта

```
ecommerce_oop/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── product.py       # Класс Product
│   │   ├── category.py      # Класс Category
│   │   └── data_loader.py   # Загрузка данных
│   └── utils/
│       ├── __init__.py
│       └── validators.py    # Валидаторы данных
├── tests/
│   ├── unit/                # Модульные тесты
│   └── integration/         # Интеграционные тесты
├── data/                    # Примеры данных
├── pyproject.toml           # Конфигурация Poetry
└── README.md                # Документация
```

Эта структура проекта обеспечивает:
- Четкое разделение на модули
- Полное покрытие тестами
- Возможность легкого расширения функционала
- Простоту использования и интеграции

## Требования

- Python 3.8+
- Poetry для управления зависимостями

## Лицензия

MIT License

## Контакты

**Автор:** Резиля Столярова
**Email:** rezilek5177@gmail.com
**GitHub:** [Rezilek](https://github.com/Rezilek)
