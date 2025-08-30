# E-commerce OOP Core

Ядро интернет-магазина с реализацией основных сущностей на ООП.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-логин/ecommerce_oop.git
   cd ecommerce_oop
   poetry install
   ```

2. Установите зависимости:
   ```bash
   poetry install
   ```

## Основные возможности

### Модели данных

#### **`Абстрактный базовый класс Product`** - класс товара
- Создан `BaseProduct` - абстрактный класс с обязательными методами
- Все классы продуктов наследуются от него
- Определяет общий интерфейс для всех продуктов
- Обработка нулевого количества в Product.init

### Миксин логирования
- Реализован `LoggingMixin` для логирования создания объектов
- Автоматически выводит информацию при создании объектов
- Добавлен в цепочку наследования класса `Product`

### Цепочка наследования:

BaseProduct (abstract) ↑ Product(LoggingMixin, BaseProduct) ↑ Smartphone,LawnGrass

#### **Smartphone (Смартфон)** - наследник Product с дополнительными полями:
   - Производительность (efficiency)
   - Модель (model)
   - Объем памяти (memory)
   - Цвет (color)

#### **LawnGrass (Газонная трава)** - наследник Product с дополнительными полями:
   - Страна-производитель (country)
   - Срок прорастания (germination_period)
   - Цвет (color)


#### **`Category`** - класс категории товаров
- Подсчет общего количества товаров
- Итерация по товарам
- Подсчитывает средний ценник всех товаров в категории
- Автоматический учет статистики
- Метод middle_price() в Category с обработкой ZeroDivisionError

#### **Валидаторы**
- `validate_price()` - проверка положительной цены
- `validate_quantity()` - проверка допустимого количества

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

# Создание товаров
phone = Product("iPhone 15", "512GB, Black", 120000, 10)
laptop = Product("MacBook Pro", "M2, 16GB", 250000, 5)

# Создание категории
electronics = Category("Электроника", "Гаджеты и устройства", [phone, laptop])

# Использование магических методов
print(phone)  # iPhone 15, 120000 руб. Остаток: 10 шт.
print(electronics)  # Электроника, количество продуктов: 15 шт.
print(phone + laptop)  # 120000*10 + 250000*5 = 2450000

# Итерация по товарам
for product in electronics:
    print(product)
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
│   │   ├── base.py          # Базовый класс моделей
│   │   ├── product.py       # Классы Product, Smartphone, LawnGrass
│   │   ├── category.py      # Класс Category
│   │   └── data_loader.py   # Загрузка данных
│   └── utils/
│       ├── __init__.py
│       └── validators.py    # Валидаторы данных
├── tests/
│   ├── unit/                # Модульные тесты
│   └── integration/         # Интеграционные тесты
├── data/                    # Примеры данных
├── .gitignore
├── pyproject.toml           # Конфигурация Poetry
└── README.md                # Документация
└── requirements.txt
```

### 🔍 Особенности реализации

- Полная документация всех методов
- Строгая типизация (mypy)
- 100% покрытие тестами
- Защищенные атрибуты
- Геттеры/сеттеры для контроля данных
- Поддержка JSON-импорта
- Магические методы для удобной работы

## Требования

- Python 3.8+
- Poetry для управления зависимостями

## Лицензия

MIT License

## Контакты

**Автор:** Резиля Столярова
**Email:** rezilek5177@gmail.com
**GitHub:** [Rezilek](https://github.com/Rezilek)
