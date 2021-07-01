from flask import Blueprint, g, render_template, request

from passageidentity import Passage, PassageError

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@auth.before_request
def before_request():
    try:
        print("starting auth")
        psg = Passage()
        print(request.headers)
        g.user = psg.authenticateRequest(request)
        print(g.user)
    except PassageError as e:
        # this is an issue with the auth check, return 401
        print("error performing auth: " + str(e))
        return render_template('unauthorized.html')

#auth.before_request(before_request)

@main.route('/')
def index():
    return render_template('index.html')

@auth.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

	
