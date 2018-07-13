# -*- coding: utf-8 -*-
"""."""
import requests
import logging

from os import environ

from .exceptions import APINotSpecified, APIKeyNotSpecified, APIConnectionError


logger = logging.getLogger(__name__)


class API(object):
    """."""
    def __init__(self, api=None, api_key=None, debug=False):
        """."""
        if api in ['cat', 'dog']:
            self.api = api
        else:
            raise APINotSpecified("Please specify API you would like to use!")

        if api_key:
            self.api_key = api_key
        else:
            api_key = environ.get("%s_API_KEY" % api.upper())
            if api_key:
                self.api_key = api_key
            else:
                raise APIKeyNotSpecified("Please specify API key!")

        self.base_url = "http://the%sapi.com/api" % api

        if debug:
            logger.setLevel("DEBUG")

    def make_request(self, url, params):
        """."""
        resp = requests.get(url, params=params)
        self.parse_status_code(resp.status_code)

    def parse_status_code(self, status_code):
        """."""
        if status_code == 200:
            return
        elif status_code == 400:
            raise APIConnectionError("Invalid format or data was specified in \
                                      request!")
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
            raise APIConnectionError("Unknown error with %d status_code" %
                                     status_code)
