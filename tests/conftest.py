"""Pytest configuration file."""
import pytest

from catdog import DogApi
from catdog import CatApi


def pytest_addoption(parser):
    """Adding cli option for pytest."""
    parser.addoption(
            "--api_name", action="store", default=None
    )

    parser.addoption(
            "--api_key", action="store", default=None
    )


@pytest.fixture(scope='session')
def api(request):
    """."""
    # reading the cli args
    api_name = request.config.getoption('--api_name')

    if api_name == 'cat':
        if request.config.getoption("--api_key"):

            # checks if the api_key arg was provided
            api_key = request.config.getoption("--api_key")

            return CatApi(api_key, debug=True)
        else:
            return CatApi(debug=True)
    elif api_name == 'dog':
        if request.config.getoption("--api_key"):

            # checks if the api_key arg was provided
            api_key = request.config.getoption("--api_key")

            return DogApi(api_key, debug=True)
        else:
            return DogApi(debug=True)
    else:
        raise Exception(
                "Please, pass api name (dog/cat) to the pytest "
                "via `--api_name={{api_name}}` cli option."
        )
