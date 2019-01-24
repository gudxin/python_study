import pymysql

db = pymysql.connect("127.28.171.128","root","lakerkobe00","TESTDB")

cursor = db.sursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version :{}".format(data))

db.close()