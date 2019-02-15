# import pymysql

<<<<<<< HEAD
# db = pymysql.connect("127.28.171.128","xiaogu","xiaogu123","mysql")

# cursor = db.sursor()

# cursor.execute("SELECT VERSION()")

# data = cursor.fetchone()

# print("Database version :{}".format(data))
=======
db = pymysql.connect("192.168.14.130","xiaogu","lakerkobe00","TESTDB")

cursor = db.cursor()

sql = """INSERT INTO ZIGBEE(HEAD,
		IP,PH,CONDI,TEMP1,TEMP2,TEMP3,TEMP4,TEMP5,TEMP6,TEMP7,TEMP8,
		PAUSE1,PAUSE2,PAUSE3,PAUSE4,PAUSE5,SPEED,THICKNESS,SUM,DATE,TAIL)
		VALUES ('ff', '172017000255', '00.00', '000.0', '617.0',
		'617.0','000.0','000.0','000.0','000.0','000.0','000.0',
		'1','1','1','1','1','00.00','0000','185','20190123083734','11')"""
		
try:
	#执行sql语句
   cursor.execute(sql)
	#提交到数据库执行
   db.commit()
except:
	#如果发生错误则回滚
   db.rollback()
   
# cursor.execute(sql)
>>>>>>> 9a566e9034f3e846cada43d2019df53681fd35de

# db.close()

<<<<<<< HEAD
import mysql.connector
 
mydb = mysql.connector.connect(
host="127.28.171.128",       # 数据库主机地址
user="root",    # 数据库用户名
passwd="lakerkobe00"   # 数据库密码
)
 
print(mydb)
=======
>>>>>>> 9a566e9034f3e846cada43d2019df53681fd35de
