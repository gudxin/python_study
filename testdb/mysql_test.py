import mysql.connector

mydb = mysql.connector.connect(
	host = "172.27.171.238",
	user = "xiaogu",
	passwd = "lakerkobe00"
)

print(mydb)