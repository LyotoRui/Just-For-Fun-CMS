from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required

control_panel = Blueprint('cp', __name__, url_prefix='/cp')




@control_panel.route('/', methods=['GET', 'POST'])
def index():
    return render_template('cp_index.html')