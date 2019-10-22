from flask import Blueprint
from flask import request
from flask import jsonify

from tag_app import log
from utils import get_request_data
from constants import ResponseStatus


errors = Blueprint('errors', __name__)

response_data = {"data": None, "status": ResponseStatus.Error}


@errors.app_errorhandler(404)
def page_not_found(e):
    response_data["error"] = str(e)
    log.exception("Error for request => url: %s, data: %s, ip: %s, method: %s"
                  % (request.url, get_request_data(request),
                     request.remote_addr, request.method))
    return jsonify(response_data), 404


@errors.app_errorhandler(500)
def internal_server_error(e):
    response_data["error"] = str(e)
    log.exception("Error for request => url: %s, data: %s, ip: %s, method: %s"
                  % (request.url, get_request_data(request),
                     request.remote_addr, request.method))
    return jsonify(response_data), 500


@errors.app_errorhandler(403)
def access_denied(e):
    response_data["error"] = str(e)
    log.exception("Error for request => url: %s, data: %s, ip: %s, method: %s"
                  % (request.url, get_request_data(request),
                     request.remote_addr, request.method))
    return jsonify(response_data), 403


@errors.app_errorhandler(400)
def bad_request(e):
    response_data["error"] = str(e)
    log.exception("Error for request => url: %s, data: %s, ip: %s, method: %s"
                  % (request.url, get_request_data(request),
                     request.remote_addr, request.method))
    return jsonify(response_data), 400


@errors.app_errorhandler(Exception)
def handle_exception(e):
    response_data["error"] = str(e)
    log.exception("Error for request => url: %s, data: %s, ip: %s, method: %s"
                  % (request.url, get_request_data(request),
                     request.remote_addr, request.method))
    return jsonify(response_data), 500
