#!api_server/bin/python
from flask import Flask,jsonify,abort,request,make_response,url_for

app = Flask("PFC_REST_API_SERVER")


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found Page' } ), 404)


@app.route('/')
def index():
	return "Hello, World It is first my api_server!"

@app.route('/v1/blynk_auth_list')
def v1_blynk_index():
	return "Hello, this is blynk index"

@app.route('/v1/<blynk_auth_token>/')
def v1_blynk_auth_token():
	return "Hello, Guyes"






if __name__ == '__main__':
	app.run(debug=True)
