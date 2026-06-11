from flask import Flask, render_template, jsonify


app = Flask(__name__)

@app.route("/")
def home():

    marks = {
        'alice': 85,
        'bob': 92,
        'charlie': 78,
        'diana': 95,
        'eve': 88,
        'frank': 91
    }
    return jsonify(marks)
    # return render_template("index.html")






app.run(debug=True)
