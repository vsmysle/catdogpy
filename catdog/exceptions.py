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


class IlligalArgumentType(Exception):
    """IlligalArgumentType.
    Raises when method gets an argument with an illigal type.
    """
    pass


class InvalidImageFile(Exception):
    """InvalidImageFile.
    Raises when file do not exist or it is a link.
    """
    pass


class UnsupportedAPIType(Exception):
    """UnsupportedAPIType.
    Raises when unknown child class inherits API class.
    """
    pass


class NotAValidDirectory(Exception):
    """NotAValidDirectory.
    Raises when directory does not exist or user don't have access to it.
    """
