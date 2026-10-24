from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['Batch-94']

collection = db["products"]

collection.insert_one({
                    "name": "Monitor", 
                    "quantity": 5
                       })

for document in collection.find():
    print(document['name'])

client.close()