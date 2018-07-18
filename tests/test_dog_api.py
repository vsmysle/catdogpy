"""
Dog API tests.
"""


def test_search(api):
    """Testing of the search method."""
    resp = api.search(limit=1)
    assert 1, len(resp)
    assert resp[0].id

    resp = api.search(limit=10)
    assert 10, len(resp)
    assert True, all(i.id for i in resp)


def test_get_image_by_id(api):
    """Testing of the get_image_by_id functionality."""
    image_id = "Hylo4Snaf"
    resp = api.get_image_by_id(image_id)
    assert 1, len(resp)
    assert image_id, resp.id


def test_upload_image(api):
    """Testing image upload functionality."""
    pass


def test_delete_image_by_id(api):
    """Testing image delete by id functionality."""
