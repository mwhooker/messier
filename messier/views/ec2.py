import json

from flask import Module, Response, abort, redirect, request
from urllib import unquote

from messier import config, defaults
from messier.lib.aws.ec2 import Connection, Instances
from messier.lib.util import paginated


conn = Connection()
ec2 = Module(__name__)

@ec2.route("/ec2/instances.json")
def list_instances():
    page = int(request.args.get("page", 1))
    per_page = request.args.get("per_page", defaults["pagination"]["per_page"])
    pages = paginated(Instances.list(conn), page, per_page)

    if not pages["items"]:
        abort(404)

    return Response(json.dumps({
        "pages": pages["pages"],
        "items": [json.loads(inst.to_json()) for inst in pages["items"]]
    }),
                    mimetype="application/json")


@ec2.route("/ec2/instances/<path:iid>.json", methods=["GET"])
def show_json(iid):
    unquoted = unquote(iid)
    return Response(Instances.instance(conn, unquoted).to_json(),
                    mimetype="application/json")
