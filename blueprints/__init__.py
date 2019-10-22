from tag_app import app
from .tags import tags
from .errors import errors

app.register_blueprint(tags)
app.register_blueprint(errors)
