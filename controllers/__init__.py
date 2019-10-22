from time import time

from flask import jsonify

from constants import ResponseStatus
from tag_app import file_handler
from utils import Log
from utils import get_request_data


class _Controller(object):

    def __init__(self, request):
        self.request = request
        self.log = Log(file_handler, self.__class__.__name__)
        self.response_data = {"data": None, "status": ResponseStatus.OK}
        self.response_status_code = 200

    def _call(self, *args, **kwargs):
        raise NotImplementedError("%s._call" % self.__class__.__name__)

    def call(self, *args, **kwargs):
        try:
            start_time = time()
            self.log.debug("Processing %s call." % self.__class__.__name__)
            result = self._call(*args, **kwargs)
            self.response_data["data"] = result
            self.log.debug("Call processed.")
        except Exception as e:
            self.log.exception(str(e))
            self.response_data["status"] = ResponseStatus.Error
            self.response_data["error"] = str(e)
            self.response_status_code = 500
        finally:
            end_time = time()
            self.response_data["time_taken"] = "%.6f" % (end_time - start_time)
            return jsonify(self.response_data), self.response_status_code

    def verify_post_data(self, parameters):
        data = get_request_data(self.request)
        for k, v in parameters.items():
            if data.get(k) in (None, ""):
                raise Exception(v)
        return data
