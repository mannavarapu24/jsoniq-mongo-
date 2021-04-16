from pymongo import MongoClient
import sys
def insertgame():
    client = MongoClient('mongodb://localhost:27017/')
    db = client["baseballDB"]
    col= db["games"]

    with open(sys.argv[1], 'r') as my_file:
        data = my_file.read()
    my_file.close()

    m1 = data.split('\n')
    col.delete_many({})

    for i in m1:
        file={}
        m2 = i.split(':')
        file["date"] = m2[0]
        file["v_code"] = m2[1]
        file["h_code"] = m2[2]
        file["v_score"] = m2[3]
        file["h_score"] = m2[4]
        col.insert_one(file)
    print("Data loaded successfully")

insertgame()