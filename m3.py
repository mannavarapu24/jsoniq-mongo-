from pymongo import MongoClient

def m3(db):
    c_no = list(db.customers.find({},{"CNO":1, "_id": 0} ))
    p={}
    for c in c_no:
        x = list(db.orders.aggregate([
            {"$match":{"CUSTOMER": int(c["CNO"]) }},
            {"$project": {"ONO": 1, "_id": 0}}

        ]))
        p[int(c["CNO"])]=x
    print(p)

client = MongoClient('mongodb://localhost:27017/')
db=client["moDB"]
m3(db);
