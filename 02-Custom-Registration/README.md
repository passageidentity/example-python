# Custom Registration Fields with Pasasge

This application is an extension of the basic Flask login application that includes separate login and registration pages, in addition to custom registration fields. This example application shows you how to add custom registration fields (in this case, a "name" field) and integrate Passage with your own database. For a full guide, see our documentation [here](https://docs.passage.id/guides/custom-registration-data).

## Configure Environment Variables

1. Get your Passage App ID and an API Key from the [Passage Console](https://console.passage.id).
2. Fill in the placeholder variables in `.flaskenv` with these values.

## Configuring a Flask Server

The [passage-identity](https://pypi.org/project/passage-identity/) package requires a Passage App ID and an optional API Key for more advanced functionality. An application's ID and API Key can be copied off of the Passage Console. In this example app, we use the environment variable to initialize the Passage SDK and in the HTML template for the login page.

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
