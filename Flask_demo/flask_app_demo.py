from flask import Flask

app = Flask(__name__)
@app.route("/index")
def home():
	return "Hi There"
	
@app.route("/SayHello/<name>")
def say_hello(name):
	return "Hello %s " %s name


app.run()
