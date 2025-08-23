class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs) -> None:
        """Инициализирует объект и логирует его создание."""
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        params = ", ".join(
            [f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args]
        )
        print(f"{class_name}({params})")

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        class_name = self.__class__.__name__
        params = ", ".join(
            [
                f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}"
                for k, v in self.__dict__.items()
                if not k.startswith("_")
            ]
        )
        return f"{class_name}({params})"
