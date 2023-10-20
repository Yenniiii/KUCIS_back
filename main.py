import pymysql
import pandas as pd

conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="1111",db="testdb",autocommit=True,charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)
cur=conn.cursor()

cur.execute("select * from member")
datas=cur.fetchall()
datas=pd.DataFrame(datas)

conn.close()
print(datas)