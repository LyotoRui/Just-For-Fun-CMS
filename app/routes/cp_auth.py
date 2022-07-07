from flask import Blueprint, render_template, request, flash

cp_auth = Blueprint("cp_auth", __name__, url_prefix="/")


@cp_auth.route("/login", methods=["GET", "POST"])
def login():
    print(request.form)
    match request.method:
        case "POST":
            if len(request.form.get('email')) > 0:
                flash('success')
            else:
                flash('error')
            return render_template('cp_login.html')
        case "GET":
            return render_template('cp_login.html')


@cp_auth.route("/logout", methods=["GET", "POST"])
def logout():
    match request.method:
        case "POST":
            pass
        case "GET":
            pass
