class BaseModel:
    """Базовый класс для всех моделей"""

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"
