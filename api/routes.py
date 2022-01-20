"""
API Routes
"""
from api import api
from api.items_api import ItemResource, DownloadableItemResource, ItemsResource

api.add_resource(ItemsResource, "/v1/items")
api.add_resource(ItemResource, "/v1/items/<item_id>")
api.add_resource(DownloadableItemResource, "/v1/items/<item_id>/download")
