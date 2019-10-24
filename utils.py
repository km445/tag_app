import logging


class Log(object):
    """File logger class"""

    def __init__(self, file_handler, log_name):
        self._log = logging.getLogger(log_name)
        self._log.addHandler(file_handler)
        self._log.setLevel(file_handler.level)

    def __getattr__(self, *args, **kwargs):
        return getattr(self._log, *args, **kwargs)


def get_request_data(request):
    return dict(request.json or request.form.items() or
                request.args.items() or {})
