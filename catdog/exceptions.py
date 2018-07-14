"""Custom exceptions module."""


class APINotSpecified(Exception):
    """APINotSpecified exception.
    Raises when API (dog/cat) was not specified.
    """
    pass


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
