# Sarah Hodge
# CS-340 Module 5
# SNHU

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port, db, col):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = password
        HOST = host
        PORT = port
        DB = db
        COL = col
        #
        # Initialize Connection
        #
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            print(data)
            createData = self.database.animals.insert_one(data) 
            if createData != 0:
                return True
            else:
                return False  
        # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"id": False})
        else:
            data = self.database.animals.find({}, {"id": False})
        return list(data)
   
    
# Create method to implement U in CRUD
    def update(self, searchData, updateData):
        if searchData is not None:
            if self.database.animals.count_documents(searchData)!=0:
                data_update = self.database.animals.update_many(searchData, {"$set" : updateData})
                updated = data_update.raw_result
            else:
                updated = "Search criteria returned no results"
            return updated
        else:
            raise Exception("Nothing to update; verify format and data entry")

# Create method to implement D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            data_delete = self.database.animals.delete_many(deleteData)
            deleted = data_delete.raw_result
            return deleted
        else:
            raise Exception("Nothing to delete; verify format and data entry")
                            