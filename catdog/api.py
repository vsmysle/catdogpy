# -*- coding: utf-8 -*-
"""API module."""
import json
import logging
from os import environ, path
from functools import wraps
import requests


from .exceptions import (APIKeyNotSpecified, APIConnectionError,
                         UnsupportedRequestType, UnsupportedAPIType,
                         IlligalArgumentType, NotAValidDirectory)


class API(object):
    """API class."""

    def __init__(self, api_key=None, debug=False):
        """API object init.

        :param api_key: API key.
        :type api_key: str
        :param debug: Debug flag (used for logging).
        :type debug: bool
        """
        class_name = self.__class__.__name__

        # setting debug as class attribute
        self.debug = debug

        # setting logger as class attribute
        self.logger = logging.getLogger(class_name)

        if api_key:
            self.api_key = api_key
        else:
            api_key = environ.get("%s_API_KEY" % class_name.upper()[:4])
            if api_key:
                self.api_key = api_key
            else:
                raise APIKeyNotSpecified("Please specify API key!")

        # check the child api name and set base_url according to it
        if class_name == "DogApi":
            self.base_url = "https://api.thedogapi.com"
        elif class_name == "CatApi":
            self.base_url = "http://thecatapi.com/api"
        else:
            raise UnsupportedAPIType(
                "%s is not supported." % class_name
            )

        self.api_version = '/v1/'
        if debug:
            self.logger.setLevel("DEBUG")

    def make_request(self, req_type, url, headers=None,
                     params=None, data=None, files=None):
        """Make request to remote API server.

        :param req_type: Request type.
        :type req_type: str

        :param url: Link to remote resource.
        :type url: str

        :param headers: Request headers.
        :type headers: dict

        :param params: Query params to a request.
        :type params: dict

        :param data: Request payload.
        :type data: dict

        :returns Response from the remote server.
        :rtype request.Response object
        """
        if not headers:
            headers = {}
        if self.api_key:
            if self.__class__.__name__ == "DogApi":
                headers['x-api-key'] = self.api_key
            else:
                params['api_key'] = self.api_key

        # check the request type
        if req_type == 'get':
            resp = requests.get(url, headers=headers, params=params)
        elif req_type == 'post':
            print(data)
            resp = requests.post(url, headers=headers, params=params,
                                 data=data, files=files)
        elif req_type == 'delete':
            resp = requests.delete(url, headers=headers, params=params,
                                   data=data)
        else:
            raise UnsupportedRequestType(
                "API only supports get, post, delete request types.")
        self.parse_status_code(resp.status_code)
        return resp

    @staticmethod
    def parse_status_code(status_code):
        """Parses response status code value.

        :param status_code: Response status code.
        :type status_code: int
        :raises APIConnectionError: if status_code != 200
        """
        if status_code == 200:
            return
        elif status_code == 400:
            raise APIConnectionError(
                "You dont have permissions to post/delete this "
                "or invalid data was specified in request!")
        elif status_code == 401:
            raise APIConnectionError("Invalid API key was provided!")
        elif status_code == 403:
            raise APIConnectionError("Connection was refused by API server!")
        elif status_code == 404:
            raise APIConnectionError("Not found!")
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
    def requires_api_key(cls, func):
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

    @staticmethod
    def check_arg_type(arg, arg_type):
        """Checks that argument value is instance of arg_type.

        :param arg: Argument value to check.
        :type arg: any

        :param arg_type: Argument class.
        :type arg_type: class

        :raises IlligalArgumentType if arg is not an instance of arg_type.
        """
        if not isinstance(arg, arg_type):
            raise IlligalArgumentType(
                "%s type is %s but it should be %s" % (
                    arg.__name__,
                    type(arg),
                    arg_type
                )
            )

    def save(self, obj, out_dir='./'):
        """Save the model to the filesystem.

        :param out_dir: Output directory.
        :type out_dir: str

        :raises NotADirectoryError if provided out_dir is not directory
        """
        if not path.isdir(out_dir):
            raise NotAValidDirectory(
                "Either %s is not a directory or you don't access to it."
            )
        # check if obj has url attribute
        if obj.url:

            # fetch file from remote server
            raw_data = self.make_request('get', obj.url)

            # compose out_file location string
            out_file_loc = ''.join([
                out_dir,
                obj.url.split('/')[-1]
            ])

            # write data to a file
            with open(out_file_loc, 'wb') as out_file:
                out_file.write(raw_data.content)
        else:
            # compose out_file location string
            out_file_loc = ''.join([
                out_dir,
                obj.__class__.__name__,
                '.json'
            ])

            # write data to a file
            with open(out_file_loc, 'a') as out_file:
                json.dump(obj.__dict__, out_file)

    def save_all(self, obj_list, out_dir="./"):
        """Save all dogs images.

        :param obj_list: List that contain objects.
        :type obj_list: list

        :param out_dir: Directory where to save images.
        :type our_dir: str
        """
        # iterate over all objects
        for obj in obj_list:
            self.save(obj, out_dir=out_dir)
