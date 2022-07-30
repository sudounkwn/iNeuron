import pandas as pd
import excelToCSV as ex
import loggerFile as lg
from sqlalchemy import create_engine

'''class that returns dataset for the excel document passed'''
try:
    class PandsDataset:
        def __init__(self,path):
            '''Initialiation method'''
            self.path = path

        def dataset_prep(self):
            '''Function that returns dataset of the excel file passed'''
            dt = pd.read_excel(self.path)
            return dt

        def dataset_ToJSON(self):
            '''Function that takes output of datasset_prep() and converts it into JSON format file'''
            ds = self.dataset_prep()
            ex1 = ex.FileConvertor(self.path)
            jsonPath = ex1.jsonPath()
            ds.to_json(jsonPath,orient='records')

        def dataset_fromDB(self):
            cnx = create_engine('mysql://Raj:Thispass@4122@localhost/mysqlassign',
                                   echo=True).connect()
            df = pd.read_sql_table('Dress_Sales',cnx)
            cnx.close()
            return df

        def dataset_ToJSON_fromDB(self):
            '''Function that takes output of DB read and converts it into JSON format file'''
            ds = self.dataset_fromDB()
            ex1 = ex.FileConvertor(self.path)
            jsonPath = ex1.jsonPath()
            ds.to_json(jsonPath,orient='records')

except Exception as e:
    lg.logg.info(e)


try:
    p =PandsDataset('C:/Users/Hp/Desktop/Raj/DataSet/data fsds/Attribute DataSet.xlsx')
    p.dataset_ToJSON() ##read fron excel document and convert to dataset and then convert to JSON format using Pandas

    p.dataset_ToJSON_fromDB()  ##read from MySQL DB and then that as input and convert to JSON file

except Exception as e:
    lg.logg.info(e)