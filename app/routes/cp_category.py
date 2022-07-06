from flask import Blueprint, render_template, request

cp_category = Blueprint("cp_category", __name__, url_prefix="categories")


@cp_category.route("/<int:id>", methods=["GET", "POST"])
def method_name(id: int):
    match request.method:
        case "POST":
            pass
        case "GET":
            pass


@cp_category.route("/add", methods=["GET", "POST"])
def add():
    match request.method:
        case "POST":
            pass
        case "GET":
            pass
