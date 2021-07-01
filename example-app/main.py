from flask import Blueprint, g, render_template, request

from passageidentity import Passage, PassageError

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@auth.before_request
def before_request():
    try:
        psg = Passage()
        g.user = psg.authenticateRequest(request)
    except PassageError as e:
        # this is an issue with the auth check, return 401
        return render_template('unauthorized.html')

#auth.before_request(before_request)

@main.route('/')
def index():
    return render_template('index.html')

@auth.route('/dashboard', methods=['GET'])
def dashboard():
    # g.user should be set here. You can then do authorization checks and show the dashboard as appropriate
    return render_template('dashboard.html')

	
