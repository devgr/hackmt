# Sample project using Vue.js, Flask, and MongoDB

## Setup using Cloud 9
- Create a workspace on c9.io 
    - Be sure to select **the HTML5 template**
    - Be sure to copy and paste this repo's git address into the "Clone from Git or Mercurial URL" box: **https://github.com/devgr/hackmt.git**
- From the terminal in your new Cloud 9 workspace, run `source setup.sh`
- Once that completes, go to the Tools menu > Preview > Preview Running Application
    - That should show a page that says "Hi!"
    - Note the URL that it loaded. That is the public URL for your Cloud 9 workspace.
    - That address is http://workspacename-username.c9users.io 
- Don't click the big green Run button.

For example:
- The address for me is http://hackmt-devgr.c9users.io
- The second demo page for me is http://hackmt-devgr.c9users.io/demo2.html
- All of the HTML and JS files are in the public directory.

## Flask API
Start the Flask Python server with `flask run`

Some environment variables are were at the end of the setup.sh file. **If opening a new terminal window later on**, be sure to run those last two lines in setup.sh again.

All requests that start with `/api` get forwarded to Flask. For example, http://hackmt-devgr.c9users.io/api/hello calls the hello function in the app.py file, in the api directory.

## MongoDB
MongoDB should already be installed from running setup.sh (it runs `mongo/mongo_setup.sh`). 

To start the database, **open a new terminal** and run `sudo ./mongo/mongo_start`

There is some test data in `mongo/data.json`. It can be loaded into the database by `cd mongo` then `./mongo_data_import.sh`

Once Mongo has been started and the data imported, the example in `api/app.py` that uses the database should work.