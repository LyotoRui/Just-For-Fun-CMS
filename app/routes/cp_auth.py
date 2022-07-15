from flask import Blueprint, jsonify, render_template, request, redirect, url_for


auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route('/auth', methods=['GET', 'POST'])
def login():
    # match request.method:
    #     case 'POST':
    #         if check_user_login(request=request):
    #             return jsonify({'success': True})
    #         else:
    #             return jsonify({'success': False})
    #     case 'GET':
    #         return render_template('cp_auth.html')
    pass

@auth.route('/logout', methods=['POST'])
def logout():
    return  redirect(url_for('cp.auth'))

