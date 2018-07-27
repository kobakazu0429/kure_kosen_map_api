# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

from backend.config import settings
from backend.flask.layer import *
from backend.flask.utils.msgs import *

from backend.flask.api.get.types import get_types
from backend.flask.api.get.groups import get_groups
from backend.flask.api.get.categories import get_categories
from backend.flask.api.get.formats import get_formats
from backend.flask.api.get.attributes import get_attributes

from backend.flask.api.post.type import post_type
from backend.flask.api.post.group import post_group
from backend.flask.api.post.category import post_category
from backend.flask.api.post.format import post_format
from backend.flask.api.post.attribute import post_attribute

from backend.flask.api.patch.type import patch_type
from backend.flask.api.patch.group import patch_group
from backend.flask.api.patch.category import patch_category
from backend.flask.api.patch.format import patch_format
from backend.flask.api.patch.attribute import patch_attribute

from backend.flask.api.delete.type import delete_type
from backend.flask.api.delete.group import delete_group
from backend.flask.api.delete.category import delete_category
from backend.flask.api.delete.format import delete_format
from backend.flask.api.delete.attribute import delete_attribute


app = Flask(__name__)
CORS(app)


# 404の時は以下を返す
@app.errorhandler(404)
def not_found(error):
    return returnError404()


# 処理する前にdbへ接続する
@app.before_request
def before_request_handler():
    db.connect()


# 処理した後にdbを切断する
@app.teardown_request
def after_request_handler(exc):
    if not db.is_closed():
        db.close()


# Routing
# GET
@app.route('/api/types/', methods=['GET'])
def api_types_get():
    return make_response(get_types())


@app.route('/api/groups/', methods=['GET'])
def api_groups_get():
    return make_response(get_groups())


@app.route('/api/categories/', methods=['GET'])
def api_categories_get():
    return make_response(get_categories())


@app.route('/api/formats/', methods=['GET'])
def api_formats_get():
    return make_response(get_formats())


@app.route('/api/attributes/', methods=['GET'])
def api_attributes_get():
    return make_response(get_attributes())


# -------------------------------------------
# POST
@app.route('/api/types/', methods=['POST'])
def api_type_post():
    return post_type(request)


@app.route('/api/groups/', methods=['POST'])
def api_group_post():
    return post_group(request)


@app.route('/api/categories/', methods=['POST'])
def api_category_post():
    return post_category(request)


@app.route('/api/formats/', methods=['POST'])
def api_format_post():
    return post_format(request)


@app.route('/api/attributes/', methods=['POST'])
def api_attribute_post():
    return post_attribute(request)


# -------------------------------------------
# PATCH
@app.route('/api/types/<int:id>/', methods=['PATCH'])
def api_type_patch(id):
    return patch_type(id, request)


@app.route('/api/groups/<int:id>/', methods=['PATCH'])
def api_group_patch(id):
    return patch_group(id, request)


@app.route('/api/categories/<int:id>/', methods=['PATCH'])
def api_category_patch(id):
    return patch_category(id, request)


@app.route('/api/formats/<int:id>/', methods=['PATCH'])
def api_format_patch(id):
    return patch_format(id, request)


@app.route('/api/attributes/<int:id>/', methods=['PATCH'])
def api_attribute_patch(id):
    return patch_attribute(id, request)


# -------------------------------------------
# DELETE
@app.route('/api/types/<int:id>/', methods=['DELETE'])
def api_type_delete(id):
    return delete_type(id)


@app.route('/api/groups/<int:id>/', methods=['DELETE'])
def api_group_delete(id):
    return delete_group(id)


@app.route('/api/categories/<int:id>/', methods=['DELETE'])
def api_category_delete(id):
    return delete_category(id)


@app.route('/api/formats/<int:id>/', methods=['DELETE'])
def api_format_delete(id):
    return delete_format(id)


@app.route('/api/attributes/<int:id>/', methods=['DELETE'])
def api_attribute_delete(id):
    return delete_attribute(id)


# -------------------------------------------
# layer
@app.route('/api/layer/', defaults={'id': None}, methods=['GET', 'POST', 'PATCH', 'DELETE'])
@app.route('/api/layer/<int:id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def swicth_layer(id):
    if request.method == 'GET':
        return make_response(get_layer(id))
    elif request.method == 'POST':
        return make_response(post_layer(request))
    elif (request.method == 'PATCH' and id is not None):
        return make_response(patch_layer(id, request))
    elif (request.method == 'DELETE' and id is not None):
        return make_response(delete_layer(id))
    else:
        return returnError404()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings.FLASK_PORT)