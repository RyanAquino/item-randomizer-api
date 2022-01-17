"""
API Routes
"""
from api.items_api import ItemResource, DownloadableItemResource, GenerateItemsResource
from api import api

api.add_resource(ItemResource, "/v1/items/<item_id>")
api.add_resource(GenerateItemsResource, "/v1/generate-items")
api.add_resource(DownloadableItemResource, "/v1/items/<item_id>/download")
