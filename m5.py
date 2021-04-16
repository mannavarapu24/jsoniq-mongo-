from pymongo import MongoClient

def m5():

    m_num = db.orders.find({"ONO":1024},{"ITEMS":1,"_id": 0} )
    total =0
    print("total sales in 1024")
    for m in m_num:
        for j in range(0,len(m["ITEMS"])):
            price = list(db.parts.find({"PNO":int(m["ITEMS"][j]["PARTNUMBER"])},{"PRICE":1,"_id": 0} ))
            total += price[0]["PRICE"] * m["ITEMS"][j]["QUANTITY"]

    print(total)

client = MongoClient('mongodb://localhost:27017/')
db=client["moDB"]

m5();