import sys
""".. 代表到上一層資料夾, 從上一層去找對應的package"""
sys.path.append("..")
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi




"""Test_LoadMongoDB"""
try:
    uri = "mongodb+srv://root:<your password>@etlcluster.shglprb.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

"""Add Data"""
try:
    db = client['ETLtest']
    collection = db['Loadtest']
    addDataResult = collection.insert_one({
        "test": "Hello World"
    })
    print("Add successful!")
    print("ObjectID:", addDataResult.inserted_id)
except Exception as e:
    print(e)

"""Check Data"""
try:
    # addDataObjectID = addDataResult.inserted_id
    getDataResult = collection.find_one(addDataResult.inserted_id)
    print("Data:",getDataResult)
    print("Check successful!")
except Exception as e:
    print(e)

"""Update Data"""
try:
    UpdateData=collection.update_one({
        "test": "Hello World"},
        {
            "$set":{
            "test": "Hello World Update"
        }
    })
    UpdateDataResult = collection.find_one(addDataResult.inserted_id)
    print("Data:",UpdateDataResult)
    print("Update successful!")    
except Exception as e:
    print(e)

"""Delete Data"""
try:
    DeleteData = collection.delete_one({
        "test": "Hello World Update"
    })
    print("Data:",DeleteData)
    print("Delete successful!")
except Exception as e:
    print(e)