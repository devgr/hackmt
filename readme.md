# Sample project using Vue.js, Flask, and MongoDB

## Setup using Cloud 9
Create a workspace on c9.io using *the HTML5 template*, and *this git repo* https://github.com/devgr/hackmt.git

After cloning this repository and navigating to it, run `source setup.sh`

Start the Flask Python server with `flask run`

Go to http://workspacename-username.c9users.io and you should see a page that says, "Hi!"

For example:
- The address for me is http://hackmt-devgr.c9users.io
- The second demo page for me is http://hackmt-devgr.c9users.io/demo2.html
- All of the HTML and JS files are in the public directory.

## Flask API
Flask should be running already from the `flask run` command. Additionally, some environment variables are were at the end of the setup.sh file. If opening a new terminal window later on, be sure to run those last two lines in setup.sh again.

All requests that start with `/api` get forwarded to Flask. For example, http://hackmt-devgr.c9users.io/api/hello calls the hello function in the app.py file, in the api directory.

## MongoDB
MongoDB should already be installed from running setup.sh, which runs `mongo/mongo_setup.sh`. To start the database, open a new terminal and run `./mongo/mongo_start`

There is some test data in `mongo/data.json`. It can be loaded into the database by `cd mongo` then `./mongo_data_import.sh`

Once Mongo has been started and the data imported, the example in `api/app.py` that uses the database should work.