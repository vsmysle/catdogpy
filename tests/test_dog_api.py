"""
Dog API tests.
"""


def test_search(api):
    """Testing of the search method.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    resp = api.search(limit=1)
    assert 1, len(resp)
    assert resp[0].id

    resp = api.search(limit=10)
    assert 10, len(resp)
    assert True, all(i.id for i in resp)


def test_get_image_by_id(api):
    """Testing of the get_image_by_id functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    image_id = "Hylo4Snaf"
    resp = api.get_image_by_id(image_id)
    assert 1, len(resp)
    assert image_id, resp.id


def test_upload_image(api):
    """Testing image upload functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # resp = api.upload_image()
    pass


def test_delete_image_by_id(api):
    """Testing image delete by id functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # resp = api.delete_image_by_id()
    pass


def test_get_images(api):
    """Testing get images functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    resp = api.get_images(limit=2)
    assert isinstance(resp, list)

    # resp = api.upload()
    # resp = api.get_images(limit=1, order='ASC')
    # assert 1, len(resp)
    # assert resp[0].id

    # resp = api.upload()
    # resp = api.get_images(limit=2, page=0, order='DESC')
    # assert 2, len(resp)


def test_get_breeds_by_image_id(api):
    """Testing get breeds by image id functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    resp = api.get_breeds_by_image_id("Hylo4Snaf")
    assert 1, len(resp)
    assert 10, resp[0].id


def test_add_breed_to_image(api):
    """Testing add breed to images functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # resp = api.add_breed_to_image()
    pass


def test_delete_breed_from_image(api):
    """Testing delete breed from image functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # resp = api.delete_breed_from_image()
    pass


def test_get_breed_by_id(api):
    """Testing get breed by id functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    resp = api.get_breed_by_id(10)
    assert 1, len(resp)
    assert resp.id, 10


def test_get_breed_list(api):
    """Testing get breed list functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    resp = api.get_breed_list()
    assert isinstance(resp, list)
    assert resp[0].id


def test_get_favourite_dogs(api):
    """Testing get favourite dogs functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # resp = api.upload()
    # resp = api.post_favourite_dogs()
    # resp = api.get_favourite_dogs()
    pass


def test_post_favouite_dogs(api):
    """Testing post favourite dogs.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # resp = api.upload()
    # resp = api.post_favourite_dogs()
    pass


def test_delete_from_favourites(api):
    """Testing delete from favourites functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # resp = api.upload()
    # resp = api.post_favourite_dogs()
    # resp = api.delete_from_favourites()
    pass


def test_get_votes(api):
    """Testing get votes functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    resp = api.get_votes()
    assert isinstance(resp, list)

    # resp = api.post_vote(image_id, sub_id)
    # resp = api.get_votes()
    # assert 1, len(resp)


def test_post_vote(api):
    """Testing post vote functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # image_id = "Hylo4Snaf"
    # resp = api.post_vote(image_id, "test_id")
    # assert isinstance(resp, dict)
    pass


def test_delete_vote(api):
    """Testing delete vote functionality.

    :param api: DogApi object instance.
    :type api: catdog.dog.DogApi
    """
    # vote_id = "Hylo4Snaf"
    # resp = api.detete_vote(vote_id)
    # assert isinstance(resp, dict)
    pass
