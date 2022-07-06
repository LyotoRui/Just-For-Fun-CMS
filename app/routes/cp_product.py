from flask import Blueprint, render_template, request

cp_product = Blueprint("cp_product", __name__, url_prefix="/product")


@cp_product.route("/<int:id>", methods=["GET", "POST"])
def method_name(id: int) -> str:
    match request.method:
        case "POST":
            pass
        case "GET":
            pass


@cp_product.route("/add", methods=["GET", "POST"])
def add():
    match request.method:
        case "POST":
            pass
        case "GET":
            pass
