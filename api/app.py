import os
from flask import Flask
app = Flask(__name__)

# http://your_workspace_name-your_username.c9users.io/hello
@app.route('/api/hello')
def hello_world():
	return 'Hello, World!'
