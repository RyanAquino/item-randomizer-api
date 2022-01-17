"""
Items API module
"""
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


class GenerateItemsResource(Resource):
    """
    Generate Items API Resource
    """
    def post(self):
        """
        Generate items and store in a file
        :return: None
        """
        return {"post": "/v1/items/generate"}
