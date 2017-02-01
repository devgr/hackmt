#!/bin/bash

# based on https://community.c9.io/t/setting-up-mongodb/1717
sudo apt-get update
sudo apt-get install -y mongodb-org
mkdir data
echo 'mongod --bind_ip=$IP --dbpath=data --nojournal --rest "$@"' > mongo_start
chmod a+x mongo_start

# Normal way to install mongo, but doesn't work well Cloud 9
# based on https://docs.mongodb.com/v3.2/tutorial/install-mongodb-on-ubuntu/
#sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
#echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
##echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
#sudo apt-get update
#sudo apt-get install -y mongodb-org
#sudo service mongod start
