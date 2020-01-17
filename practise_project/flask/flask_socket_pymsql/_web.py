from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import pymysql


# 配置数据库连接
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
	db = pymysql.connect("192.168.14.130", "xiaogu", "lakerkobe00", "TESTDB")
	cursor = db.cursor()
	sql = "SELECT * FROM zigbee"
	cursor.execute(sql)
	u = cursor.fetchall()
	# db.close()
	return render_template('index.html', u=u)

if __name__ == '__main__':
	app.run()