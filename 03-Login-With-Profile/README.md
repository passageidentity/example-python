# Using Passage with Python

Passage provides a Python package to easily authenticate HTTP requests. This folder is an example of how to use Passage in a Python Flask web application. It uses the Passage Auth element for login and registration and the Passage Profile element for the user dashboard.

## Configure Environment Variables

1. Get your Passage App ID and an API Key from the [Passage Console](https://console.passage.id).
2. Fill in the placeholder variables in `.flaskenv` with these values.

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

## Run With Docker

Make sure you have [docker installed on your computer](https://docs.docker.com/get-docker/).

Create your docker image:

```bash
$ docker build -t example-python .
```

Run your docker container using the example-python image, changing the port numbers as necessary:

```bash
$ docker run -p 5000:5000 example-python
```

You can now visit http://localhost:5000 in your browser to see Passage in action.

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

## Adding Authentication to the Frontend

The easiest way to add authentication to a web frontend is with a Passage Element. The HTML below will automatically embed a complete UI/UX for user sign-in and sign-up. In this example application, we automatically use the PASSAGE_APP_ID environment variable in the `app-id` attribute.

```html
<!-- Passage will populate this custom element with a complete authentication UI/UX. -->
<passage-auth app-id="<Passage App ID>"></passage-auth>

<!-- Include the passage-web JavaScript from the Passage CDN. -->
<script src="https://cdn.passage.id/passage-web.js"></script>
```

To add the Profile Element to the dashboard, do the following:
```html
<!-- Passage will populate this custom element with a complete profile UI/UX. -->
<passage-profile app-id="<Passage App ID>"></passage-profile>

<!-- Include the passage-web JavaScript from the Passage CDN. -->
<script src="https://cdn.passage.id/passage-web.js"></script>
```
