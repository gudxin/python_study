import pymysql

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

db.close()

