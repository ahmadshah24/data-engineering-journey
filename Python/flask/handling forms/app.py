from flask import Flask, render_template,request



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "POST"):
        with open("data.txt", "a") as f:
            f.write(f"{request.form['name']} - {request.form['email']}\n")
        return render_template("index.html")
    else:
        return render_template("index.html")

    # print(request.method)
    # print(request.form)






app.run(debug=True)
