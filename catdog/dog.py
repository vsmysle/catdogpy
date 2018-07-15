"""DogApi module."""
from os import path

from .api import API
from .exceptions import InvalidImageFile
from .models import Animal, Breed, Category, Dog


class DogApi(API):
    """DogApi class."""

    def __init__(self, *args, **kwargs):
        """DogApi object init."""
        super().__init__(*args, **kwargs)

    def search(self, breed_id=None, mine_types=None, limit=1):
        """Search dogs using various filters.

        :param breed_id: Breed id.
        :type breed_id: int

        :param mine_types: Image extensions to search.
        :type mine_types: list

        :param limit: Number of images to search.
        :type limit: int

        :return dogs: Fetched dogs.
        :type dogs: list
        """

        valid_mine_types = ['gif', 'jpg', 'png']
        if mine_types not in valid_mine_types:
            mine_types = None
        else:
            mine_types = ', '.join(mine_types)

        if not isinstance(limit, int):
            limit = 1

        # combining search url
        search_url = ''.join([
            self.base_url,
            self.api_key,
            'search'
        ])

        params = {}

        # filling the params dict
        for arg in self.search.__code__.co_varnames:
            if eval(arg):
                params[arg] = eval(arg)

        # fetching Dogs from API
        resp = self.make_request(search_url, params)

        # convert response data to python dict
        resp_data = resp.json()

        dogs_list = []

        for dog in resp_data:
            dogs_list.append(self.process_response(dog))

        return dogs_list

    def get_image_by_id(self, image_id):
        """Get dog image by image_id.

        :param image_id: Dog image id.
        :type image_id: str
        """
        # compose endpoint url
        url = ''.join([
            self.base_url,
            self.api_version,
            'images/',
            image_id
        ])

        # make request to remote server
        resp = self.make_request('get', url)

        # convert response to python dict
        resp_data = resp.json()

        dog = self.process_response(resp_data)
        return dog

    @API.requires_api_key
    def upload_image(self, filepath, sub_id=None, breed_ids=None):
        """Upload Dog image to the API.

        :param filepath: Path to the image.
        :type filepath: str

        :param sub_id: Image owner identificator.
        :type sub_id: str

        :param breed_ids: Breeds of the dogs in the image.
        :type breed_ids: list

        :return resp: ???
        :rtype: ???
        """
        # check that args have valid type
        if self.debug:
            self.check_arg_type(filepath, str)

        # compose endpoint url
        url = ''.join([
            self.base_url,
            self.api_version,
            'images/upload'
        ])

        # check that file exists and it is not a link
        if not path.isfile(filepath) or path.islink(filepath):
            raise InvalidImageFile(
                "File do not exist or it is a link!"
            )

        files = {'file': open(filepath, 'rb')}

        headers = {'Content-Type': 'multipart/form-data'}

        data = {}

        if sub_id:
            # check that sub_id has correct type
            self.check_arg_type(sub_id, str)
            data['sub_id'] == sub_id

        if breed_ids:
            # check that breed_ids has correct type
            self.check_arg_type(breed_ids, list)
            data['breed_ids'] == breed_ids

        resp = self.make_request('post', url, params=data, files=files,
                                 headers=headers)
        return resp

    @API.requires_api_key
    def delete_image_by_id(self, image_id):
        """Delete dog image from the API.

        :param image_id: Image identificator.
        :type image_id: str

        :return resp: ???
        :rtype: ???
        """
        # checking the type of image_id var if debug mode is on
        if self.debug:
            self.check_arg_type(image_id, str)

        # compose endpoint url
        url = ''.join([
            self.base_url,
            self.api_version,
            'image/',
            image_id
        ])

        # delete an image from a API
        resp = self.make_request('delete', url)
        return resp

    def get_images(self, limit=1, page=0, order='DESC'):
        """Get dog images from the API.

        :param limit: Length of return images list.
        :type limit: int

        :param page: Pagination parameter.
        :type page: int

        :param order: Order of the return images list.
        :type order: str

        :return dogs_list: List of Dog objects.
        :rtype: list
        """
        # compose endpoint url
        url = ''.join([
            self.base_url,
            self.api_version,
            'images/'
        ])

        # set default limit value if it is not int
        if not isinstance(limit, int):
            limit = 1

        # set default page value if it is not int
        if not isinstance(page, int):
            page = 0

        # check that order value is valid
        if order not in ['DESC', 'ASC']:
            order = 'DESC'

        params = {}

        # filling the params dict
        for arg in self.search.__code__.co_varnames:
            if eval(arg):
                params[arg] = eval(arg)

        # make request to API server
        resp = self.make_request('get', url, params)

        # convert return data to python dict
        dogs_data = resp.json()

        return [self.process_response(dog) for dog in dogs_data]

    def get_breeds_by_image_id(self, image_id):
        """Get dog breeds from an image.

        :param image_id: Dog image identificator.
        :type image_id: str

        :return list_: List of Breed objects.
        :rtype: list
        """
        # check that args have correct type
        if self.debug:
            self.check_arg_type(image_id, str)

        # compose endpoint url
        url = ''.join([
            self.base_url,
            self.api_version,
            'images/',
            image_id,
            '/breeds'
        ])

        # make get request to the API
        resp = self.make_request('get', url)

        # convert response data to python dict
        breeds_data = resp.json()

        return [Breed(**breed) for breed in breeds_data]

    @API.requires_api_key
    def add_breed_to_image(self, image_id, breed_id):
        """Add dog breed to dog image.

        :param image_id: Dog image identificator.
        :type image_id: str

        :param breed_id: Dog breed identificator.
        :type breed_id: int

        :return resp: ???
        :rtype: ???
        """
        # check that args have correct type
        if self.debug:
            self.check_arg_type(image_id, str)
            self.check_arg_type(breed_id, int)

        # compose endpoint url
        url = ''.join([
            self.base_url,
            self.api_version,
            'images/',
            image_id,
            '/breeds'
        ])

        # compose data payload dict
        data = {'breed_id': breed_id}

        # make request to API server
        resp = self.make_request('post', url, data=data)
        return resp

    @API.requires_api_key
    def delete_breed_from_image(self, breed_id):
        """."""
        pass

    def save_all_images(self, dogs_list):
        """."""
        pass

    def get_breed_by_id(self, breed_id):
        """."""
        pass

    def get_breed_list(self):
        """."""
        pass

    def get_favourite_dog_by_id(self, dog_image_id):
        """."""
        pass

    def get_favourite_dogs(self):
        """."""
        pass

    @API.requires_api_key
    def post_favourite_dogs(self, dog_image_id, sub_id=None):
        """."""
        pass

    @API.requires_api_key
    def delete_dog_from_favourites_by_id(self, dog_image_id, sub_id=None):
        """."""
        pass

    def get_votes(self):
        """."""
        pass

    def get_vote_by_id(self):
        """."""
        pass

    @API.requires_api_key
    def post_vote(self, dog_image_id, sub_id=None):
        """."""
        pass

    @API.requires_api_key
    def delete_vote_by_id(self, dog_image_id, sub_id=None):
        """."""
        pass

    @staticmethod
    def process_response(resp_data):
        """Creates Dog object from response data.

        :param resp_data: Response data.
        :type resp_data: dict
        :return dog: Dog object.
        :rtype: models.Dog
        """
        animals = []
        breeds = []
        categories = []

        # if images has info regarding dogs breeds
        try:
            if resp_data['breeds']:

                # iterate over all breeds
                for breed in resp_data['breeds']:

                    # append Breed objects
                    breeds.append(
                        Breed(**breed)
                    )
        except KeyError:
            pass

        # if images has info regarding animals
        try:
            if resp_data['animals']:

                # iterate ovel all animals
                for animal in resp_data['animals']:

                    # append Animal objects
                    animals.append(
                        Animal(**animal)
                    )
        except KeyError:
            pass

        # if images has info regarding dogs categories
        try:
            if resp_data['categories']:

                # iterate over all categories
                for category in resp_data['categories']:
                    print(category)
                    # append Category objects
                    categories.append(
                        Category(**category)
                    )
        except KeyError:
            pass

        dog_data = {
            'id': resp_data['id'],
            'url': resp_data['url'],
            'image_width': resp_data['width'],
            'image_height': resp_data['height'],
            'breeds': breeds,
            'animals': animals,
            'categories': categories
        }

        dog = Dog(**dog_data)
        return dog
