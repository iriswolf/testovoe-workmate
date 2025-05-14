class DomainError(Exception): ...


class DomainFieldError(DomainError):
    """
    Для ошибок валидации значений в полях value objects,
    entities и нарушения инвариантов
    """
