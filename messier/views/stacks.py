import json

from flask import Module, Response, redirect, request
from urllib import unquote

from messier import config
from messier.lib.aws.cloudformation import Connection, Stacks


conn = Connection()
stacks = Module(__name__)


@stacks.route("/stacks.json")
def list_json():
    return Response(json.dumps([json.loads(stack.to_json())
                                for stack in Stacks.list(conn)]),
                    mimetype="application/json")


@stacks.route("/stacks/<path:sid>.json", methods=["GET"])
def show_json(sid):
    unquoted = unquote(sid)
    stack = Stacks.stack(unquoted, conn)
    return Response(stack.to_json(), mimetype="application/json")


@stacks.route("/stacks/<path:sid>.json", methods=["DELETE"])
def delete_json(sid):
    unquoted = unquote(sid)
    Stacks.delete(unquoted, conn)
    stack = Stacks.stack(unquoted, conn)
    return Response(stack.to_json(), mimetype="application/json")


@stacks.route("/stacks/new", methods=["POST"])
def new_stack():
    name = request.form["stackName"]
    template = request.files["stackTemplate"].stream.getvalue()
    Stacks.new_stack(name, template, conn)
    return redirect("/stacks")
