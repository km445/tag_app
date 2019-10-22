import logging
from datetime import datetime

logs_dir = "logs"
log_config = {"level": logging.DEBUG,
              "filename": ("%s/logs_%s.log" %
                           (logs_dir, datetime.now().strftime("%Y-%m-%d"))),
              "format": (logging
                         .Formatter("%(asctime)s [%(thread)d:%(threadName)s] "
                                    "[%(levelname)s] - %(name)s: %(message)s"))
              }

# flask app secret key
secret_key = 'secret_key'
