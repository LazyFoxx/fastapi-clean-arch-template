class ApplicationError(Exception):
    """Базовый класс для application ошибок"""


class EmailAlreadyExistsError(ApplicationError):
    """Email уже занят"""

    def __init__(self, email: str):
        super().__init__(f"Email уже используется: {email}")
        self.email = email


class InvalidTokenError(ApplicationError):
    pass


class UserNotFoundError(ApplicationError):
    pass
