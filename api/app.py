import os
import json
from flask import Flask, Response, request
from data_access import DB
import bson.json_util as mongo_json
app = Flask(__name__)

# http://your_workspace_name-your_username.c9users.io/hello
@app.route('/api/hello')
def hello_world():
	return 'Hello, World!'

	
# route to return some hard coded Rogue One data
@app.route('/api/example')
def example():
	data = {
		'name': 'Jyn Erso',
		'height': '160',
		'hair_color': 'brown',
		'skin_color': 'light',
		'eye_color': 'green',
		'birth_year': '22BBY',
		'gender': 'female',
		'homeworld': 'Vallt'
	}
	string_data = json.dumps(data)
	return Response(string_data, content_type='text/json; charset=utf-8')


# get the same thing out of mongo
@app.route('/api/rogueone/<name>')
def rogueone(name):
	db = DB()
	jyn = db.get_character(name)
	string_data = mongo_json.dumps(jyn)
	return Response(string_data, content_type='text/json; charset=utf-8')


@app.route('/api/example', methods=['POST'])
def example_post():
	data = request.get_json()
	return Response(json.dumps(data), content_type='text/json; charset=utf-8')
	
@app.route('/api/rogueone', methods=['POST'])
def rogueone_post():
	data = request.get_json()
	# it would be smart to check the data to make sure it is valid.
	db = DB()
	db.add_character(data)
	return '', 200