"""
API Routes
"""
from api import api
from api.items_api import DownloadableItemResource, ItemsResource

api.add_resource(ItemsResource, "/v1/item")
api.add_resource(DownloadableItemResource, "/v1/item/download")
