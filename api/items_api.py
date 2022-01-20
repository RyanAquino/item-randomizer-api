"""
Items API module
"""
import os
import string
from random import choice, randint, uniform
from typing import Optional

from flask_restful import Resource


class ItemResource(Resource):
    """
    Item API Resource
    """
    def get(self, item_id: int):
        """
        Retrieve Item object details
        :param item_id: Item id
        :return: Item object details
        """
        return {"get": f"/v1/items/{item_id}"}


class DownloadableItemResource(Resource):
    """
    Downloadable file Item API Resource
    """
    def get(self, item_id: int):
        """
        Retrieve Item object file
        :param item_id: Item id
        :return: Item object file
        """
        return {"get": f"/v1/items/{item_id}/download"}


class ItemsResource(Resource):
    """
    Generate Items API Resource
    """
    @staticmethod
    def _generate_random_alphabet_strings(n: Optional[int] = 10) -> str:
        """
        Generate a random alphabetical string
        :param n: Number of characters to be generated; default to 10
        :return: Generated random alphabetical string
        """
        return "".join(choice(string.ascii_letters) for _ in range(n))

    @staticmethod
    def _generate_random_real_numbers() -> str:
        """
        Generate random real number in between of values 1.5 to 1.9
        :return: Generated real number in string format
        """
        return str(uniform(1.5, 1.9))

    @staticmethod
    def _generate_random_integers() -> str:
        """
        Generate a random integer from range 100,000 to 900,000
        :return: Generated random integer in string format
        """
        return str(randint(100000, 900000))

    @staticmethod
    def _generate_random_alphanumerics(n: Optional[int] = 10) -> str:
        """
        Generate a random alphanumeric string
        :return: Generated alphanumeric string
        """
        return "".join(choice(f"{string.ascii_letters}0123456789") for _ in range(n))

    def post(self):
        """
        Generate items and store in a file with 2MB size
        :return: file name
        """
        file_name = "output.txt"
        file_size_buffer = 10000
        max_file_size = ((1024 * 1024) * 2) - file_size_buffer  # 2MB
        open(file_name, "w")
        file_size = os.stat(file_name).st_size

        with open(file_name, 'w') as f:
            f.truncate()
            while file_size <= max_file_size:
                func_list = [
                    self._generate_random_alphabet_strings,
                    self._generate_random_real_numbers,
                    self._generate_random_integers,
                    self._generate_random_alphanumerics
                ]
                output = choice(func_list)()
                f.write(f"{output}, ")
                file_size = os.stat(file_name).st_size

            f.close()
        return {"file_name": file_name}, 201
