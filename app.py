#!api_server/bin/python
from flask import Flask,jsonify,abort,request,make_response,url_for,request
import json
import sys
from time import time


DB_FILE_NAME = 'pfc_log_data.log'
TOKEN_FILE_NAME = 'token_list.txt'

def sensor_db_insert(authtoken,key,value,unix_ts):
	# print('this is error test ! ', file=sys.stderr)
	with open(DB_FILE_NAME,"a") as logf:
		log_raw = authtoken +',' + key + ',' + value  +','+unix_ts + "\r\n"
		logf.write(log_raw)		



app = Flask("PFC_REST_API_SERVER")

query_string = {
	'sensor' : [
		'at',
		'ah',
		'wt',
		'ph',
		'ec',
		'ldr',
		'co2',
	],
	'actuator' : {
		'led',
		'air_fan',
		'ventil_fan',
		'water_pump',
		'ph_plus_pump',
		'ph_minus_pump',
		'sol_a_pump',
		'sol_b_pump',
		'ptc_heater',
		'chiller',
	}
}


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

@app.route('/v1/all_data', methods=['GET'])
def v1_get_all_data():
	with open(DB_FILE_NAME) as logf:
		log_list = logf.readlines()

	return "<br>".join(log_list)




@app.route('/v1/<blynkauthtoken>/insert/', methods=['GET','POST'])
def v1_blynk_auth_token(blynkauthtoken):
	with open(TOKEN_FILE_NAME) as f:
		token_list = [line.rstrip() for line in f]


	if request.method == 'GET':
		unix_ts = str(int(time()))
		for key in request.args:
			if key in query_string['sensor']:
				sensor_db_insert(blynkauthtoken,key,request.args[key],unix_ts)
		return json.dumps(request.args)
		# request.form['hum']
		# request.form['temp']
		# request.form['ph']
		# request.form['ec']

		return "this is GET request"
	elif request.method == 'POST':
		return "this is POST request"



	if blynkauthtoken not in token_list:
		return "Token is not exists on our list!" 



	return "Exsits"




	# def login():
 #    error = None
 #    if request.method == 'POST':
 #        if valid_login(request.form['username'],
 #                       request.form['password']):
 #            return log_the_user_in(request.form['username'])
 #        else:
 #            error = 'Invalid username/password'
 #    # the code below is executed if the request method
 #    # was GET or the credentials were invalid
 #    return render_template('login.html', error=error)



if __name__ == '__main__':
	app.run(host='210.92.91.225',debug=True)
