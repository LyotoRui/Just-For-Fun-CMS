from flask import Blueprint, jsonify, render_template, request

auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route('/auth', methods=['GET', 'POST'])
def login():
    match request.method:
        case 'POST':
            login = request.form.get('login')
            password = request.form.get('password')
            if login == 'admin':
                return jsonify({'success': True})
            else:
                return jsonify({'success': False})
        case 'GET':
            return render_template('cp_auth.html')

@auth.route('/log_out', methods=['POST'])
def method_name():
    pass
