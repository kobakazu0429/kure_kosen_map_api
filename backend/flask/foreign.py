# -*- coding: utf-8 -*-
import datetime

from flask import jsonify

from backend.models.Type import *
from backend.models.Group import *
from backend.models.Category import *
from backend.models.Format import *
from backend.models.Attribute import *

from backend.flask.utils.msgs import *


def return_this(foreign):
    if (foreign == 'types'):
        return [Type(), 'type']
    elif (foreign == 'groups'):
        return [Group(), 'group']
    elif (foreign == 'categories'):
        return [Category(), 'category']
    elif (foreign == 'formats'):
        return [Format(), 'format']
    elif (foreign == 'attributes'):
        return [Attribute(), 'attribute']
    else:
        return


def get_foreign(foreign):
    data = []

    this = return_this(foreign)
    this_Class = this[0]

    for x in this_Class.select().order_by(this_Class.id).dicts():
        data.append(x)

    return jsonify(data)


def post_foreign(foreign, request):
    if (foreign == 'types'):
        Type.create(
            type=request.form['type'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        ),
    elif (foreign == 'groups'):
        Group.create(
            group=request.form['group'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        ),
    elif (foreign == 'categories'):
        Category.create(
            category=request.form['category'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        ),
    elif (foreign == 'formats'):
        Format.create(
            format=request.form['format'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        ),
    elif (foreign == 'attributes'):
        Attribute.create(
            attribute=request.form['attribute'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        ),
    else:
        return returnError404()

    return returnResultCreate()


def patch_foreign(foreign, id, request):
    this = return_this(foreign)
    this_Class = this[0]

    patching_foreign = this_Class.get_by_id(id)

    if (foreign == 'types'):
        patching_foreign.type = request.form['type']
        patching_foreign.updated_at = datetime.datetime.now()
    elif (foreign == 'groups'):
        patching_foreign.group = request.form['group']
        patching_foreign.updated_at = datetime.datetime.now()
    elif (foreign == 'categories'):
        patching_foreign.category = request.form['category']
        patching_foreign.updated_at = datetime.datetime.now()
    elif (foreign == 'formats'):
        patching_foreign.format = request.form['format']
        patching_foreign.updated_at = datetime.datetime.now()
    elif (foreign == 'attributes'):
        patching_foreign.attribute = request.form['attribute']
        patching_foreign.updated_at = datetime.datetime.now()
    else:
        return returnError404()

    patching_foreign.save()

    return returnResultPatch()


def delete_foreign(foreign, id):
    this = return_this(foreign)
    this_Class = this[0]

    deleting_foreign = this_Class.get_by_id(id)

    deleting_foreign.delete_instance()

    return returnResultDelete()
