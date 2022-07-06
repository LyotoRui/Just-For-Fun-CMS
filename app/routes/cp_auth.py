from flask import Blueprint, render_template, request

cp_auth = Blueprint("cp_auth", __name__, url_prefix="/auth")


@cp_auth.route("/login", methods=["GET", "POST"])
def login():
    match request.method:
        case "POST":
            pass
        case "GET":
            pass


@cp_auth.route("/logout", methods=["GET", "POST"])
def logout():
    match request.method:
        case "POST":
            pass
        case "GET":
            pass
