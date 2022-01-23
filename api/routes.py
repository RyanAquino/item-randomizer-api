"""
API Routes
"""
from flask_swagger_ui import get_swaggerui_blueprint

from api import api, app
from api.items_api import DownloadableItemResource, ItemsResource

SWAGGER_URL = "/api-docs"
API_URL = "/static/swagger.yaml"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Item Randomizer API"}
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

api.add_resource(ItemsResource, "/v1/item")
api.add_resource(DownloadableItemResource, "/v1/item/download")
