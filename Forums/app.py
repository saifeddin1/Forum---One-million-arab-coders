from forums import dummy_data
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


if (__name__ ) == "__main__":
	
    app.run(debug = True)
