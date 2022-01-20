"""
API Routes
"""
from api import api
from api.items_api import ItemResource, DownloadableItemResource, ItemsResource

api.add_resource(ItemsResource, "/v1/items")
api.add_resource(ItemResource, "/v1/items/<int:item_id>")
api.add_resource(DownloadableItemResource, "/v1/item/download")
