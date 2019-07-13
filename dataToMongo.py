#!/usr/bin/env python
import pandas as pd
import pymongo
import json
import os

def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['stocks']  # Replace mongo db name
    collection_name = 'stocksItems'  # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    
    #drop collection stockItems
    print(db_cm)
    
    #update records
    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    #db_cm.delete_one()
    db_cm.insert_many(data_json)

if __name__ == "__main__":
    # pass csv file path
    filepath = 'C:/Users/jjara/Desktop/virtual_workspace/pennystocks/dataMongoUpload.csv'
    import_content(filepath)
