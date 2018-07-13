"""."""
from .api import API


class Dog(API):
    """Dog class."""

    def __init__(self):
        """Dog object init."""

    def search(self, breed_id=None, mine_types=None, limit=1):
        """Search dogs using various filters.

        :param breed_id: Breed id.
        :type breed_id: int

        :param mine_types: Image extensions to search.
        :type mine_types: list

        :param limit: Number of images to search.
        :type limit: int
        """

        valid_mine_types = ['gif', 'jpg', 'png']
        if mine_types not in valid_mine_types:
            mine_types = None
        else:
            mine_types = ', '.join(mine_types)

        if not isinstance(limit, int):
            limit = 1

        search_url = self.base_url + '/v1/search'

        # TODO
        # params = [x if x for x in self.search.__code__.co_varnames]

        resp = self.make_request(search_url, params)

    def get_by_id(self, image_id):
        """Get dog by image_id.

        :param image_id: Dog image id.
        :type image_id: str
        """
        pass

    def upload(self, filepath, sub_id=None, breed_ids=None):
        """Upload Dog image to the API.

        :param filepath: Path to the image.
        :type filepath: str

        :param sub_id: Image owner identificator.
        :type sub_id: str

        :param breed_ids: Breeds of the dogs in the image.
        :type breed_ids: list
        """
        pass

    def delete(self, dog_id):
        """."""
        pass
