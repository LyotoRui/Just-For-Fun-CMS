from flask import Blueprint, render_template, request

cp_settings = Blueprint("cp_settings", __name__, url_prefix="/settings")


@cp_settings.route("/", methods=["GET", "POST"])
def show_settings():
    match request.method:
        case "POST":
            pass
        case "GET":
            pass
