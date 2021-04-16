from pymongo import MongoClient
import sys
def insertteams():

    client = MongoClient('mongodb://localhost:27017/')
    db = client["baseballDB"]
    col= db["teams"]

    with open(sys.argv[1], 'r') as m1_file:
        data = m1_file.read()
    m1_file.close()

    m1 = data.split('\n')
    col.delete_many({})

    for i in m1:
        file={}
        m2 = i.split(':')

        file["name"] = m2[0]
        file["location"] = m2[1]
        file["code"] = m2[2]
        col.insert_one(file)
    print("Data inserted successfully")
insertteams()