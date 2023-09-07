import sys
""".. 代表到上一層資料夾,從上一層去找對應的package"""
sys.path.append("..")
import package.ExtractPostgreSQL 
import package.TransformData
import package.sentenceBERT
import package.LoadMongoDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



start_date = "2021-12-15"
end_date = "2021-12-20"
search = "萊豬"

"""Test_ExtractPostgreSQL.searchKeyword()"""
try:
    totalData = package.ExtractPostgreSQL.searchKeyword(start_date, end_date, search)
    print("PostgreSQL connection successful!")
except Exception as e:
    print(e)

"""Test_TransformData.dataclean.first_clean()"""
try:
    df = package.TransformData.dataclean.first_clean(totalData)
    df_list = df.values.tolist()
    print("first_clean successful!")
except Exception as e:
    print(e)

"""Test_sentenceBERT.semanticSimilarity"""
try:
    pairs = package.sentenceBERT.semanticSimilarity(df_list)
    print("semanticSimilarity successful!")
except Exception as e:
    print(e)

"""Test_TransformData.dataclean.second_clean()"""
try:
    pairs = package.TransformData.dataclean.second_clean(pairs)
    print("second_clean successful!")
except Exception as e:
    print(e)

"""Test_ConnectMongoDB"""
try:
    uri = "mongodb+srv://root:<your password>@etlcluster.shglprb.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)