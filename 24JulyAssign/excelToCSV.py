import pandas as pd
import loggerFile as lg

'''Code to convert Excel dataset document to CSV file for uploading into DB'''

try:
    class FileConvertor:
        def __init__(self, path):
            '''Initialization of paths of Excel file and in the same path CSV file to be stored'''
            self.path = path

        def csvPath(self):
            '''Function to convert Excel to CSV and store it inside the MySQL Data folder for importing to DB'''
            xlpathList = self.path
            xlpathList = xlpathList.replace('xlsx', 'csv')
            return xlpathList

        def csvFile(self):
            xlpathList = self.path
            lis = xlpathList.split("\\")
            return (lis[len(lis)-1].replace('xlsx', 'csv'))

        def jsonPath(self):
            '''Function to convert Excel to CSV and store it inside the MySQL Data folder for importing to DB'''
            xlpathList = self.path
            xlpathList = xlpathList.replace('xlsx', 'json')
            return xlpathList

        def XLtoCSV(self):
            '''Function that reads Excel file and calls interal function csvPath to create csv file'''
            tempf = pd.read_excel(self.path)
            tempf.fillna(value='Null',method=None,inplace=True,limit=None,downcast=None)
            tempf.to_csv(self.csvPath(), index=None, header=True)

except Exception as e:
    lg.logg.info(e)