from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	greeting = "Hello World"
	return render_template("index.html", greeting=greeting)

# def hello_world():
# 	return  'Hello ,World!'

if __name__ == "__main__":
	app.run()