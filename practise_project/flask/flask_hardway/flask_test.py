from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql



# 配置数据库连接



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.14.130:3306/TESTDB'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route("/")
def index():
	# greeting = "Hello World"
	# return render_template("index.html", greeting=greeting)
	db = pymysql.connect("192.168.14.130", "xiaogu", "lakerkobe00", "TESTDB")
	cursor = db.cursor()
	sql = "SELECT * FROM zigbee"
	cursor.execute(sql)
	u = cursor.fetchall()
	db.close()
	return render_template('index.html', u=u)

if __name__ == "__main__":
	app.run()