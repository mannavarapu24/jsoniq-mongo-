from pymongo import MongoClient

def m4():

    e_num = list(db.employees.find({"CITY":"Wichita"},{"ENO":1, "_id": 0} ))

    for e in e_num:
        c_no = list(db.orders.find({"TAKENBY":int(e["ENO"])},{"CUSTOMER":1, "_id": 0} ))

    c_name=[]

    for c in c_no:
        c_name.append(list(db.customers.find({"CNO":int(c["CUSTOMER"])},{"CNAME":1, "_id": 0} )))
    print(c_name)

client = MongoClient('mongodb://localhost:27017/')
db=client["moDB"]

m4();