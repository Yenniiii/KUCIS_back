import pymysql
import pandas as pd

conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="1111",db="testdb",autocommit=True,charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)
cur=conn.cursor()

#read
cur.execute("select * from member")
datas=cur.fetchall()
datas=pd.DataFrame(datas)

#create
#프론트에서 받아와서 처리
user_name1='이예은'
sql="insert into `member`(`name`) values(%s)"
#cur.execute(sql,user_name1)

cur.execute("select * from member")
datas=cur.fetchall()
datas=pd.DataFrame(datas)

#update 
user_name2='최나경'
sql="update `member` set `name` =%s where `name`=%s"
cur.execute(sql,(user_name2,user_name1))

#delete
sql="delete from `member` where `name`=%s"
cur.execute(sql,user_name2)

cur.execute("select * from member")
datas=cur.fetchall()
datas=pd.DataFrame(datas)

conn.close()
print(datas)