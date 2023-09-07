from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

"""輸入 MongoDB 連線位址"""
uri = "mongodb+srv://root:<your password>@etlcluster.shglprb.mongodb.net/?retryWrites=true&w=majority"

"""Create a new client and connect to the server"""
client = MongoClient(uri, server_api=ServerApi('1'))

"""
client['資料庫名稱']
db['collection名稱']
"""
db = client['資料庫名稱']
collection = db['collection名稱']

"""將語意相似度分析後的資料匯入MongoDB"""
def insertData(pairs):
    pairs.reset_index(inplace=True)
    pairs = pairs.to_dict("records")
    collection.insert_many(pairs)

