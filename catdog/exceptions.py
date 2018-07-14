"""Custom exceptions module."""


class APIKeyNotSpecified(Exception):
    """APIKeyNotSpecified exception.
    Raises when API key was not specified.
    """
    pass


class APIConnectionError(Exception):
    """APIConnectionError.
    Raises when response (from remote server) status code
    doesn't equal to 200 OK.
    """
    pass


class UnsupportedRequestType(Exception):
    """UnsupportedRequestType.
    Raises when request type is not in ['get', 'post', 'delete'].
    Both APIs don't have endpoints that require other request type.
    """
    pass
