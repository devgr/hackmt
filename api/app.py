import os
import json
from flask import Flask, Response
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
@app.route('/api/rogueone')
def rogueone():
	db = DB()
	jyn = db.get_character('Jyn Erso')
	string_data = mongo_json.dumps(jyn)
	return Response(string_data, content_type='text/json; charset=utf-8')
