# Using Passage with Python

Passage provides a Python package to easily authenticate HTTP requests. This repo is an example of how to use Passage in a Python Flask web application.

## Configuring a Flask Server
The `passageidentity` package depends on a PASSAGE_PUBLIC_KEY environment variable being set. An app's PASSAGE_PUBLIC_KEY can be copied off of the Passage Console.
To run this example app, make a virtual environment and run the following commands (the environment variables are stored in `.flaskenv`).

```bash
Go ahead and create a virtual environment by typing
>> python3 -m venv venv
Once it is created, you must now activate the environment by using:
>> source venv/bin/activate
Install Python dependencies
>> pip install -r requirements.txt
Run the web server
>> flask run
```

## Authenticating an HTTP Request
A Python server can easily authenticate an HTTP request using the Passage SDK, as shown below.

```python
@auth.before_request
def before_request():
    try:
        # use passage to set the user handle
        psg = Passage()
        g.passageHandle = psg.authenticateRequest(request)
    except PassageError as e:
        # this is an issue with the auth check, return 401
        return render_template('unauthorized.html')

@auth.route('/home')
def authenticatedEndpoint():
    user = g.passageHandle
	# Successful authentication. Proceed...

}
```

## Authorizing a User
It is important to remember that the psg.authenticateRequest() function validates that a request is properly authenticated, but makes no assertions about who it is authorized for. To perform an authorization check, the Passage User Handle can be referenced.
In the above example, it would look something like this:

```python
# Check that the user with `passageHandle` is allowed to perform
# a certain action on a certain resource.
try:
    authorizationCheck(g.passageHandle)
except:
    return render_template("unauthorized.html")

# Successful authentication AND authorization. Proceed...

}
```

## Adding Authentication to the Frontend
The easiest way to add authentication to a web frontend is with a Passage Element. The HTML below will automatically embed a complete UI/UX for user sign-in and sign-up.

```html
<!-- Passage will populate this div with a complete authentication UI/UX. -->
<div id="passage-auth" data-app="<Passage App Handle>"></div>

<!-- Include the passage-web JavaScript from the Passage CDN. -->
<script src="https://cdn.passage.id/passage-web.js"></script>
```