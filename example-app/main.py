from flask import Blueprint, g, render_template, request
import os
from passageidentity import Passage, PassageError

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

# Passage setup
PASSAGE_API_KEY = os.environ.get("PASSAGE_API_KEY")
PASSAGE_APP_ID = os.environ.get("PASSAGE_APP_ID")
try:
    psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
except PassageError as e:
    print(e)
    exit()

@auth.before_request
def before_request():
    try:
        g.user = psg.authenticateRequest(request)
    except PassageError as e:
        # this is an issue with the auth check, return 401
        return render_template('unauthorized.html')

#auth.before_request(before_request)

@main.route('/')
def index():
    return render_template('index.html', psg_app_id=PASSAGE_APP_ID)

@auth.route('/dashboard', methods=['GET'])
def dashboard():
    # g.user should be set here. You can then do authorization checks and show the dashboard as appropriate

    # use Passage to get the user information and add it to the dashboard
    psg_user = psg.getUser(g.user)

    identifier = ""
    if psg_user.email:
        identifier = psg_user.email
    elif psg_user.phone:
        identifier = psg_user.phone

    return render_template('dashboard.html', identifier=identifier)

	
