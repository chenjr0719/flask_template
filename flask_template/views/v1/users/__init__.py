from flask import Blueprint, jsonify, request

v1_users_api = Blueprint("users_api", __name__, url_prefix="/v1/users/")


@v1_users_api.route("", methods=["GET"])
def list_users():
    users = [{"id": 1, "name": "Foo"}]
    return jsonify(users)
