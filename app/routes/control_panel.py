from flask import Blueprint, render_template, request

control_panel = Blueprint("control_panel", __name__)


@control_panel.route("/", methods=["GET", "POST"])
@control_panel.route("index", methods=["GET", "POST"])
def index():
    match request.method:
        case "POST":
            pass
        case "GET":
            pass
