"""."""


class Dog(object):
    """Dog class."""

    def __init__(self, image_id, url, image_width, image_height,
                 mine_types, animals=[], breeds=[], categories=[]):
        """Dog object init.

        :param image_id: Id of the dog image.
        :type image_id: str
        :param url: Url of the dog image source.
        :type url: str
        :param image_width: Width of the dog image.
        :type image_width: int
        :param image_height: Height of the dog image.
        :type image_height: int
        :param mine_type:
        """
        self.image_id = image_id
        self.url = url
        self.image_width = image_width
        self.image_height = image_height
        self.mine_types = mine_types
        self.breeds = breeds
        self.animals = animals
        self.categories = categories
        self.breed_ids = [breed.id for breed in breeds]

    def __repr__(self):
        """Represents dog in human-readable way."""
        pass

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

    def __init__(self, breed_id, name, wiki_url):
        """Breed object init.

        :param breed_id: Breed id.
        :type breed_id: int
        :param name: Breed name.
        :type name: str
        :param wiki_url: Link to breed's wikipedia page.
        :type wiki_url: str
        """
        self.breed_id = breed_id
        self.name = name
        self.wiki_url = wiki_url

    def __repr__(self):
        """Represents breed obj in a human-readable way."""
        pass


class Category(object):
    """Category class."""

    def __init__(self, category_id, name):
        """Category object init.

        :param category_id: Category id.
        :type category_id: int
        :param name: Category name.
        :type name: str
        """
        self.category_id = category_id
        self.name = name

    def __repr__(self):
        """Represents category obj in a human-readable way."""
        pass


class Animal(object):
    """Animal class."""

    def __init__(self, animal_id, name):
        """Animal object init.

        :param animal_id: Animal id.
        :type animal_id: int
        :param name: Animal name.
        :type name: str
        """
        self.animal_id = animal_id
        self.name = name

    def __repr__(self):
        """Represents animal obj in a human-readable way."""
