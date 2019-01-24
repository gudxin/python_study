import pymysql

db = pymysql.connect("127.28.171.128","xiaogu","xiaogu123","mysql")

cursor = db.sursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version :{}".format(data))

db.close()

# import mysql.connector
 
# mydb = mysql.connector.connect(
   # host="127.28.171.128",       # 数据库主机地址
   # user="root",    # 数据库用户名
   # passwd="lakerkobe00"   # 数据库密码
 # )
 
# print(mydb)