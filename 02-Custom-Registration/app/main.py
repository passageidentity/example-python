from flask import  Blueprint, g, render_template, request, jsonify
import os
from passageidentity import Passage, PassageError
from app.models import User
from app import db

# blueprint for auth routes in our app
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

@main.route('/login')
def index():
    return render_template('index.html', psg_app_id=PASSAGE_APP_ID)


@main.route('/register')
def register():
    return render_template('register.html', psg_app_id=PASSAGE_APP_ID)

@auth.route('/dashboard', methods=['GET'])
def dashboard():
    # g.user should be set here. 

    # use Passage ID to get user record in DB (name)
    user = User.query.filter_by(passage_id=g.user).first()

    # use Passage SDK to get info stored in Passage (email)
    psg_user = psg.getUser(g.user)


    return render_template('dashboard.html', name=user.name, email=psg_user.email)

@auth.route('/user', methods=['POST'])
def createUser():
    # g.user should be set here.
    u = User()
    u.passage_id = g.user
    # get name from the request
    u.name = request.get_json()["name"]
    print(u.name)
    print(u.passage_id)
    # commit to database
    try:
        db.session.add(u)
        db.session.commit()
    except Exception as e:
        print(e)

    return jsonify({"result": 200})

