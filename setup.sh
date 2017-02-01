# Run with the source command, for example: source setup.sh
# This way, the environment variables that get exported below are set in the shell that called this script.

# set up mongo database

# set up nginx web server
sudo cp nginx_conf /etc/nginx/sites-enabled/default
sudo cp nginx_conf /etc/nginx/sites-available/default
sudo service nginx restart

# set python3 as the default
echo "alias python=python3" >> ~/.bashrc
alias python=python3

# set up Flask http://flask.pocoo.org/docs/0.12/installation/#installation
sudo pip install virtualenv # install the virtual environment package
virtualenv -p /usr/bin/python3 venv # create a python virtual environment
. venv/bin/activate # enable the virtual environment
# `deactivate` to stop the virtual environment

pip install Flask # install Flask into the virtual environment

# Environment variables that are needed for Flask!
# Once these are set, and the virtual environment is enabled (see above), you can start Flask with: flask run
export FLASK_APP=api/app.py # set the default main file for a flask application
export FLASK_DEBUG=1 # run flask in debug mode. Do not use in production!