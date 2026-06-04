from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/shah")
def shah_page():
    return render_template("shah.html")


app.run(debug=True)
