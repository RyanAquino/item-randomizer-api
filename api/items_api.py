"""
Items API module
"""
import string
from random import choice, randint, uniform
from uuid import uuid4
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
    def _generate_random_alphabet_strings(n: Optional[int] = 10):
        """
        Generate a random alphabetical string
        :param n: Number of characters to be generated; default to 10
        :return: Generated random alphabetical string
        """
        return "".join(choice(string.ascii_letters) for _ in range(n))

    @staticmethod
    def _generate_random_real_numbers():
        """
        Generate random real number in between of values 1.5 to 1.9
        :return: Generated real number
        """
        return uniform(1.5, 1.9)

    @staticmethod
    def _generate_random_integers():
        """
        Generate a random integer from range 100,000 to 900,000
        :return: Generated random integer
        """
        return randint(100000, 900000)

    def _generate_random_alphanumerics(self):
        pass

    def post(self):
        """
        Generate items and store in a file
        :return: None
        """
        file_name = str(uuid4())
        file_size = (1024 * 1024) * 2  # 2MB

        with open(f"generated_items/{file_name}.txt", 'w') as f:
            num_chars = file_size
            # Add unless reach/over total file size
            # Get len + 1 (comma)

        return {"id": file_name}, 201
