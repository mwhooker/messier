from flask import Module, make_response, render_template


frontend = Module(__name__)


@frontend.route("/", defaults={"path": ""})
@frontend.route("/<path:path>")
def index(path):
    return make_response(open("messier/templates/index.html").read())
