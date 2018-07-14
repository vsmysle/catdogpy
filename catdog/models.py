"""Models module."""


class Dog(object):
    """Dog class."""

    def __init__(self, **kwargs):
        """Dog object init.

        :param **kwargs: Arbitraty keyword arguments.
        :type **kwargs: dict
        """
        self.__dict__.update(kwargs)

    def __getattr__(self, key):
        """."""
        return None

    def __repr__(self):
        """Represents dog in human-readable way."""
        return '<%s id=%s keys=%s>' % (self.__class__.__name__,
                                       self.id,
                                       str(self.__dict__.keys()))

    def save(self, filename=None):
        """Downloads the dog image from the API.

        :param filename: Output file filename.
        :type filename: str
        :return status: Image download status.
        :rtype: bool
        """
        pass


class Breed(object):
    """Breed class."""

    def __init__(self, **kwargs):
        """Breed object init.

        :param **kwargs: Arbitraty keyword arguments.
        :type **kwargs: dict
        """
        self.__dict__.update(kwargs)

    def __getattr__(self, key):
        """."""
        return None

    def __repr__(self):
        """Represents breed obj in a human-readable way."""
        return '<%s id=%i keys=%s>' % (self.__class__.__name__,
                                       self.id,
                                       str(self.__dict__.keys()))


class Category(object):
    """Category class."""

    def __init__(self, **kwargs):
        """Category object init.

        :param **kwargs: Arbitraty keyword arguments.
        :type **kwargs: dict
        """
        self.__dict__.update(kwargs)

    def __getattr__(self, key):
        """."""
        return None

    def __repr__(self):
        """Represents category obj in a human-readable way."""
        return '<%s id=%i keys=%s>' % (self.__class__.__name,
                                       self.id,
                                       str(self.__dict__.keys()))


class Animal(object):
    """Animal class."""

    def __init__(self, **kwargs):
        """Animal object init.

        :param **kwargs: Arbitraty keyword arguments.
        :type **kwargs: dict
        """
        self.__dict__.update(kwargs)

    def __getattr__(self, key):
        """."""
        return None

    def __repr__(self):
        """Represents animal obj in a human-readable way."""
        return '<%s id=%i keys=%s>' % (self.__class__.__name__,
                                       self.id,
                                       str(self.__dict__.keys()))
