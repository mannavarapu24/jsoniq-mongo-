from pymongo import MongoClient


def m1(database):

    m = database["parts"]
    getPnameQuery = m.find({'PRICE': {"$lt": 20}}, {'PNAME': 1})

    for s in getPnameQuery:
        print(s)
if __name__=="__main__":
    myclient = MongoClient('mongodb://localhost:27017/')
    database = myclient["moDB"]
    m1(database);