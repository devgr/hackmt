from pymongo import MongoClient

# tutorial on using pymongo https://api.mongodb.com/python/current/tutorial.html
class DB:
    def __init__(self):
        if not hasattr(self, 'client'):
            # if we don't already have a connection to the database, make a connection
            self.client = MongoClient() # pass other parameters here if not the default database server
            self.db = self.client.HackMT # access the HackMT database
            #self.db.authenticate(username, password) # Authenticate, if that is enabled for the database
            self.characters = self.db.rogueone # access the rogueone collection in the HackMT database
    
    def add_character(self, character):
        result = self.characters.insert_one(character)
        new_id = result.inserted_id
        return new_id
        
    def get_characters(self):
        query = self.characters.find()
        all_characters = [c for c in query]
        return all_characters
        
    def get_character(self, name):
        the_character = self.characters.find_one({'name': name})
        return the_character