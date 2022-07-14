from flask import Blueprint, request, jsonify, render_template

control_panel = Blueprint('control_panel', __name__, url_prefix='/cp')

