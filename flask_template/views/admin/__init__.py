from flask import Blueprint
from flask_template import app

admin_blueprint = Blueprint("admin_blueprint", __name__, url_prefix="/admin")


@admin_blueprint.route("/configs", methods=["GET"])
def get_configs():
    configs = {key: str(value) for key, value in app.config.items()}
    return configs
