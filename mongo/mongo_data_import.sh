mongo HackMT --eval 'db.rogueone.drop();'
mongoimport -d HackMT -c rogueone --jsonArray data.json