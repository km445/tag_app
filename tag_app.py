import os
import logging

from flask import Flask

import config
from utils import Log

app = Flask(__name__)
app.secret_key = config.secret_key

if not os.path.exists(config.logs_dir):
    os.mkdir(config.logs_dir)

file_handler = logging.FileHandler(config.log_config.get("filename"))
file_handler.setLevel(config.log_config.get("level"))
file_handler.setFormatter(config.log_config.get("format"))

log = Log(file_handler, "Tag API")
log.info("Tag API started.")

import blueprints
