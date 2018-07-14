# -*- coding: utf-8 -*-
"""API module."""
import requests
import logging

from os import environ
from functools import wraps

from .exceptions import APIKeyNotSpecified, APIConnectionError


logger = logging.getLogger(__name__)


class API(object):
    """API class."""

    def __init__(self, api_key=None, debug=False):
        """API object init.

        :param api_key: API key.
        :type api_key: str
        :param debug: Debug flag (used for logging).
        :type debug: bool
        """

        child_class_name = self.__class__.__name__
        if api_key:
            self.api_key = api_key
        else:
            api_key = environ.get("%s_API_KEY" % child_class_name.upper())
            if api_key:
                self.api_key = api_key
            else:
                raise APIKeyNotSpecified("Please specify API key!")

        self.base_url = "http://the%sapi.com/api" % child_class_name.lower()
        self.api_version = '/v1/'
        if debug:
            logger.setLevel("DEBUG")

    def make_request(self, req_type, url, params):
        """Make request to remote API server.

        :param req_type: Request type.
        :type req_type: str
        :param url: Link to remote resource.
        :type url: str
        :param params: Query params to a request.
        :type params: dict
        :returns Response from the remote server.
        :rtype request.Response object
        """
        resp = requests.get(url, params=params)
        self.parse_status_code(resp.status_code)
        return resp

    def parse_status_code(self, status_code):
        """Parses response status code value.

        :param status_code: Response status code.
        :type status_code: int
        :raises APIConnectionError: if status_code != 200
        """
        if status_code == 200:
            return
        elif status_code == 400:
            raise APIConnectionError(
                "Invalid format or data was specified in request!")
        elif status_code == 401:
            raise APIConnectionError("Invalid API key was provided!")
        elif status_code == 403:
            raise APIConnectionError("Connection was refused by API server!")
        elif status_code == 429:
            raise APIConnectionError("Too many requests!")
        elif status_code == 500:
            raise APIConnectionError("Internal error!")
        elif status_code == 502:
            raise APIConnectionError("API server is not working!")
        else:
            raise APIConnectionError(
                    "Unknown error with %d status_code" % status_code)

    @classmethod
    def requires_api_key(self, func):
        """Function decorator that helps to check if api_key value is not None.

        :param func: Function prior to which apply decorator.
        :type func: callable
        :returns decorated: if api_key value is not None.
        :rtype: callable
        """
        @wraps(func)
        def decorated(*args):
            """Checks if the api_key value is not None.

            :param args: Function arguments.
            :type args: list
            :raises APIKeyNotSpecified: if the api_key value is None.
            """
            self = args[0]
            if not self.api_key:
                raise APIKeyNotSpecified(
                    "You should provide API key for using this method!")
            func(*args)
        return decorated
