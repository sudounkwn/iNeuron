import mysql.connector as mysqlcnct
import pandas as pd
import loggerFile as lg

try:
    conn = mysqlcnct.connect(host='localhost', database='mysqlassign', user='root', password='Thispass@4122')
    cur = conn.cursor()

########################################################   6th Assign #####################################################
    cur.execute('''Select * from attrdataset a
                    left join dresssales d
                    on a.Dress_ID=d.Dress_ID''')

    val = cur.fetchall()
    print(pd.DataFrame(val))
########################################################################################################################################################################

########################################################   7th Assign #####################################################

    cur.execute('''select * from attrdataset
                    group by Dress_ID
                    order by Dress_ID;''')

    print(pd.DataFrame(cur.fetchall()))

########################################################################################################################################################################

########################################################   8th Assign #####################################################

    cur.execute('''select COUNT(*) from attrdataset
                    where Recommendation=0;''')

    print(cur.fetchone())

########################################################################################################################################################################

########################################################   9th Assign #####################################################


except Exception as e:
    lg.logg.info(e)

finally:
    if conn.is_connected():
        cur.close()
        conn.close()