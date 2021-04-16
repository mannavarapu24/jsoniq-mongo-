from pymongo import MongoClient
from flask import Flask
from flask_cors import CORS

app = Flask('__name__')
CORS(app)

@app.route('/baseball/standings/', methods=['GET'])
def stand():

    client = MongoClient('mongodb://localhost:27017/')
    db = client["baseballDB"]

    t1 = list(db.teams.find({}, {"_id": 0}))

    g1 = list(db.games.find({}, {"_id": 0}))

    final = {"standings": []}

    for t in t1:
        x = {}
        wins = 0
        loss = 0
        draw = 0

        for g in g1:
            if g["h_code"] == t["code"]:
                if int(g["h_score"]) > int(g["v_score"]):
                    wins = wins + 1
                elif int(g["h_score"]) < int(g["v_score"]):
                    loss = loss + 1
                else:
                    draw = draw + 1
            if g["v_code"] == t["code"]:

                if int(g["v_score"]) > int(g["h_score"]):
                    wins = wins + 1
                elif int(g["v_score"]) < int(g["h_score"]):
                    loss = loss + 1
                else:
                    draw = draw + 1

        x["losses"] = loss
        x["percent"] = round((wins + (draw * 0.5)) / (wins + loss + draw), 3)
        x["tcode"] = t["code"]
        x["ties"] = draw
        x["tname"] = t["name"]
        x["wins"] = wins

        final["standings"].append(x)
    return final

@app.route('/baseball/results/<string:tcode>/', methods=['GET'])
def get_result(tcode):

    client = MongoClient('mongodb://localhost:27017/')
    db = client["baseballDB"]

    t1 = list(db.teams.find({}))
    g1 = list(db.games.find({}))

    res = {"results": []}

    for g in g1:
        y = {}
        if tcode == g["v_code"]:
            y["gdate"] = g["date"]
            y["opponent"] = g["h_code"]
            if g["v_score"] > g["h_score"]:
                y["result"] = "WIN"
            elif g["v_score"] < g["h_score"]:
                y["result"] = "LOSS"
            else:
                y["result"] = "TIE"
            y["them"] = g["h_score"]
            y["us"] = g["v_score"]
            res["results"].append(y)
        if tcode == g["h_code"]:
            y["gdate"] = g["date"]
            y["opponent"] = g["v_code"]
            if g["h_score"] > g["v_score"]:
                y["result"] = "WIN"
            elif g["h_score"] < g["v_score"]:
                y["result"] = "LOSS"
            else:
                y["result"] = "TIE"
            y["them"] = g["v_score"]
            y["us"] = g["h_score"]
            res["results"].append(y)
    for t in t1:
        if tcode == t["code"]:
            res["tloc"] = t["location"]
            res["tname"] = t["name"]

    return res

if __name__ == '__main__':
    app.run(host='localhost',port=5000)