"""
Items API module
"""
import os
import string
from random import choice, randint, uniform
from typing import Optional

from flask import send_file
from flask_restful import Resource


class DownloadableItemResource(Resource):
    """
    Downloadable file Item API Resource
    """

    def get(self):
        """
        Retrieve Item object file
        :return: Item object file
        """
        file_name = "output.txt"
        file_path = f"../{file_name}"

        if not os.path.exists(file_name):
            return {"detail": "File not found"}, 404

        response = send_file(
            path_or_file=file_path,
            mimetype="application/octet-stream",
            as_attachment=True,
            attachment_filename=file_name
        )
        return response


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

        with open(file_name, 'w') as f:
            f.truncate()
            file_size = os.stat(file_name).st_size
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

        return {"file_name": file_name}, 201

    def get(self):
        """
        Retrieve Item object details
        :return: Item object details
        """
        # Count alphabet strings
        # Count real numbers
        # Count integers
        # Count alphanumeric strings
        return {"get": f"/v1/item"}
