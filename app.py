#!api_server/bin/python

from flask import Flask

app = Flask("PFC_REST_API_SERVER")

@app.route('/')
def index():
	return "Hello, World It is first my api_server!"


if __name__ == '__main__':
	app.run(debug=True)