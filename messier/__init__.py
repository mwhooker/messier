import os

from flask import Flask, Markup


def application_file(fn, prefix=".."):
    return os.path.join(os.path.dirname(__file__), prefix, fn)


app = Flask(__name__, instance_relative_config=True)
try:
    app.config.from_object("messier.default_settings")
except ImportError:
    pass

app.config.from_pyfile(os.environ.get("MESSIER_CONFIG",
                                      application_file("/etc/messier.cfg")),
                       silent=True)
app.debug = os.environ.get("FLASK_DEBUG", app.config.get("DEBUG", False))
config = app.config

defaults = {
    "pagination": {
        "per_page": 15
    }
}

from messier.views.ec2 import ec2
app.register_blueprint(ec2)
from messier.views.frontend import frontend
app.register_blueprint(frontend)
from messier.views.stacks import stacks
app.register_blueprint(stacks)
