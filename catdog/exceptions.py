"""Custom exceptions module."""


class APINotSpecified(Exception):
    """."""
    def __init__(self, message):
        super().__init__(message)


class APIKeyNotSpecified(Exception):
    """."""
    def __init__(self, message):
        super().__init__(message)


class APIConnectionError(Exception):
    """."""
    def __init__(self, message):
        super().__init__(message)
