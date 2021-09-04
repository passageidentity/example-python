# Using Passage with Python

Passage provides a Python package to easily authenticate HTTP requests. This repo is an example of how to use Passage in a Python Flask web application.

## Configuring a Flask Server
The [passage-identity](https://pypi.org/project/passage-identity/) package depends on a PASSAGE_APP_ID environment variable being set. An application's ID can be copied off of the Passage Console. In this example app, we use the environmnet variable to initialize the Passage SDK and in the HTML template for the login page. 

To run this example app, make a virtual environment and run the following commands (the environment variables are stored in `.flaskenv`).

```bash
Go ahead and create a virtual environment by typing
>> python3 -m venv venv

Once it is created, you activate the environment by using:
>> source venv/bin/activate

Install Python dependencies
>> pip install -r requirements.txt

Run the web server
>> flask run
```

## Authenticating an HTTP Request
A Python server can easily authenticate an HTTP request using the Passage SDK, as shown below. You must pass the Passage app ID when initializing
the Passage object. If you would like to use management functionality like getting user information, you must also provide an API key, which can be generated in the Passage console. To authenticate a request, an API key is NOT required.

```python
@auth.before_request
def before_request():
    try:
        # use passage to set the user ID
        psg = Passage(psg_app_id)
        g.passageUserID = psg.authenticateRequest(request)
    except PassageError as e:
        # this is an issue with the auth check, return 401
        return render_template('unauthorized.html')

@auth.route('/home')
def authenticatedEndpoint():
    user = g.passageUserID
	# Successful authentication. Proceed...

```

## Authorizing a User
It is important to remember that the `psg.authenticateRequest()` function validates that a request is properly authenticated, but makes no assertions about who it is authorized for. To perform an authorization check, the Passage User ID can be referenced.
In the above example, it would look something like this:

```python
# Check that the user with `passageUserID` is allowed to perform
# a certain action on a certain resource.
try:
    authorizationCheck(g.passageUserID)
except:
    return render_template("unauthorized.html")

# Successful authentication AND authorization. Proceed...

}
```

## Get User
 To get user information, you can use the Passage SDK with an API key. This will authenticate your web server to Passage and grant you management
 access to user information. API keys should never be hard-coded in source code, but stored in environment variables or a secrets storage mechanism.

```python
@auth.before_request
def before_request():
    try:
        # use passage to set the user ID
        psg = Passage(psg_app_id, psg_api_key)
        g.passageUserID = psg.authenticateRequest(request)
    except PassageError as e:
        # this is an issue with the auth check, return 401
        return render_template('unauthorized.html')

@auth.route('/home')
def authenticatedEndpoint():
    user = psg.getUser(g.passageUserID)
	print(user.email)
```

## Adding Authentication to the Frontend
The easiest way to add authentication to a web frontend is with a Passage Element. The HTML below will automatically embed a complete UI/UX for user sign-in and sign-up. In this example application, we automatically use the PASSAGE_APP_ID environment variable in the `data-app` attribute.

```html
<!-- Passage will populate this div with a complete authentication UI/UX. -->
<div id="passage-auth" data-app="<Passage App ID>"></div>

<!-- Include the passage-web JavaScript from the Passage CDN. -->
<script src="https://cdn.passage.id/passage-web.js"></script>
```