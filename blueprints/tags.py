from flask import Blueprint
from flask import request

from controllers.tags.get_tags import GetTagsController


tags = Blueprint("tags", __name__)


@tags.route("/get_tags", methods=["POST"])
def get_tags():
    return GetTagsController(request).call()
