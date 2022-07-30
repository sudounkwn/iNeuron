import loggerFile as lg             #import loggerFile for logging
import excelToCSV as ex             #import excelToCSV for converting file to CSV

import mysql.connector as mysqlcnct

try:
    conn = mysqlcnct.connect(host='localhost', database='mysqlassign', user='root', password='Thispass@4122')
    cur = conn.cursor()
    cur.execute('''create table IF NOT EXISTS attrDataset(Dress_ID INT,
							Style varchar(20),
                            Price varchar(20),
                            Rating varchar(20),
                            Size varchar(20),
                            Season varchar(20),
                            Neckline varchar(20),
                            Sleevelength varchar(20),
                            waiseline varchar(20),
                            Material varchar(20),
                            FabricType varchar(20),
                            Decoration varchar(20),
                            PatternType varchar(20),
                            Recommendation INT);
''')

    cur.execute('''create table IF NOT EXISTS dressSales(Dress_ID INT,
    							`29/08/2013` INT,
                                `31/08/2013` INT,
                                `09/02/2013` INT,
                                `09/04/2013` INT,
                                `09/06/2013` INT,
                                `09/08/2013` INT,
                                `09/10/2013` INT,
                                `09/12/2013` INT,
                                `14/09/2013` INT,
                                `16/09/2013` INT,
                                `18/09/2013` INT,
                                `20/09/2013` INT,
                                `22/09/2013` INT,
                                `24/09/2013` INT,
                                `26/09/2013` INT,
                                `28/09/2013` INT,
                                `30/09/2013` INT,
                                `10/02/2013` INT,
                                `10/04/2013` INT,
                                `10/06/2013` INT,
                                `10/08/2013` INT,
                                `10/10/2013` INT,
                                `10/12/2013` INT);
    ''')


    x = ex.FileConvertor('C:\ProgramData\MySQL\MySQL Server 8.0\Data\mysqlassign\Attribute DataSet.xlsx')
    y = ex.FileConvertor('C:\ProgramData\MySQL\MySQL Server 8.0\Data\mysqlassign\Dress Sales.xlsx')
    x.XLtoCSV()
    y.XLtoCSV()
    y.csvFile()

    c1 = "load data infile '"+x.csvFile()
    c2 = "' into table attrdataset FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '' LINES TERMINATED BY '\\n' IGNORE 1 ROWS;"
    cur.execute(c1+c2)

    c1 = "load data infile '"+y.csvFile()
    c2 = "' into table dressSales FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '' LINES TERMINATED BY '\\n' IGNORE 1 ROWS;"
    cur.execute(c1+c2)

    conn.commit()


except Exception as e:
    lg.logg.info(e)

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
