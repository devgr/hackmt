import os
import json
from flask import Flask, Response
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


# one route to get basically the same thing out of mongo

