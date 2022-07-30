import pymongo
import json
import loggerFile as lg

'''Insert into MongoDB of the json converted data'''

try:
    class MongodbInsert:
        def __init__(self,path):
            self.path = path

        client = pymongo.MongoClient(
            "mongodb+srv://sudounkwn:Thispass4122@raj.fbnqu.mongodb.net/?retryWrites=true&w=majority")

        db = client['mongotest']
        coll = db['test']


        def mongodb_Insert(self):
            '''Insert teh content of JSON file into Mongodb by iterating through all the sets'''
            with open(self.path) as fil:
                jsonData = json.load(fil)
            # print(jsonData)
            for i in jsonData:
                self.coll.insert_one(i)

except Exception as e:
    # mblog.log.info(e)
    lg.logg.info(e)


try:
    m=MongodbInsert('C:/Users/Hp/Desktop/Raj/DataSet/data fsds/Attribute DataSet.json')
    m.mongodb_Insert()
except Exception as e:
    # mblog.log.info(e)
    lg.logg.info(e)