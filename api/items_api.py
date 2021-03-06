"""
Items API module
"""
import os
import re
import string
from random import choice, randint, uniform

from flask import send_file
from flask_restful import Resource

from api.validators import Item


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
            attachment_filename=file_name,
        )
        return response


class ItemsResource(Resource):
    """
    Generate Items API Resource
    """

    file_name = "output.txt"

    @staticmethod
    def _generate_random_alphabet_strings() -> str:
        """
        Generate a random alphabetical string of length 10
        :return: Generated random alphabetical string
        """
        return "".join(choice(string.ascii_letters) for _ in range(10))

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
    def _generate_random_alphanumerics() -> str:
        """
        Generate a random alphanumeric string of length 10
        :return: Generated alphanumeric string
        """
        return "".join(
            choice(f"{string.ascii_letters}{string.digits}") for _ in range(10)
        )

    def post(self):
        """
        Generate items and store in a file with 2MB size
        :return: file name
        """
        file_size_buffer = 10000
        max_file_size = ((1024 * 1024) * 2) - file_size_buffer  # 2MB

        with open(self.file_name, "w") as f:
            f.truncate()
            file_size = os.stat(self.file_name).st_size
            while file_size <= max_file_size:
                func_list = [
                    self._generate_random_alphabet_strings,
                    self._generate_random_real_numbers,
                    self._generate_random_integers,
                    self._generate_random_alphanumerics,
                ]
                output = choice(func_list)()
                f.write(f"{output}, ")
                file_size = os.stat(self.file_name).st_size

        return {"file_name": self.file_name}, 201

    def get(self):
        """
        Retrieve Item object details
        :return: Item object details
        """
        response = Item()

        if not os.path.exists(self.file_name):
            return {"detail": "File not found"}, 404

        with open(self.file_name) as f:
            contents = f.read()
            content_items = contents.split(", ")
            content_items = content_items[:-1]

            for item in content_items:
                if item.isalpha():
                    response.alphabet += 1
                    continue

                if item.isalnum() and not item.isalpha() and not item.isdigit():
                    response.alphanumeric += 1
                    continue

                item_found = re.findall("[0-9]+", item)

                if item_found and item_found[0] == item:
                    response.integers += 1
                else:
                    response.real_numbers += 1

        return response.dict()
