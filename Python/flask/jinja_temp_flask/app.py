from flask import Flask, render_template


# app = Flask(__name__, static_url_path='/public') # to change the default static folder url path from /static to /public
app = Flask(__name__, static_folder='assets', static_url_path='/static') # to change the default static folder name from 'static' to 'assets'

@app.route("/")
def home():

    marks = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78
    }
    return render_template("index.html", marks=marks)



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")









app.run(debug=True)
