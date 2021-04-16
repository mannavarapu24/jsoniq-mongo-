from pymongo import MongoClient

def m6():
    m_num = db.orders.find({})
    final={}
    for e in m_num:
        total = 0
        for m in range(0,len(e["ITEMS"])):
            p = list(db.parts.find({"PNO":int(e["ITEMS"][m]["PARTNUMBER"])},{"PRICE":1,"_id": 0} ))
            total += p[0]["PRICE"] * e["ITEMS"][m]["QUANTITY"]
        if e["TAKENBY"] in final:
            final[e["TAKENBY"]] += total
        else:
            final[e["TAKENBY"]] = total
    print(final)

client = MongoClient('mongodb://localhost:27017/')
db=client["moDB"]

m6();