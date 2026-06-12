from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}


app = Flask(__name__)
UPLOAD_FOLDER = './user_uploads' # Directory to save uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/create", methods=["GET", "POST"])
def create():
    my_id = uuid.uuid1()

    if request.method == "POST":
        recive_id = request.form.get("uuid")
        decsripation = request.form.get("text")
        input_files = []
        for key, value in request.files.items():
            file = request.files[key]

            if file and file.filename != "":
                filename = secure_filename(file.filename)

                folder_path = os.path.join(app.config["UPLOAD_FOLDER"], recive_id)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                filepath = os.path.join(folder_path, filename)
                file.save(filepath)
                input_files.append(filename)
            with open(os.path.join(app.config["UPLOAD_FOLDER"], recive_id, "description.txt"), "w") as desc_file:
                desc_file.write(decsripation)

        for file in input_files:
            with open(os.path.join(app.config["UPLOAD_FOLDER"],recive_id , 'input.txt'), "a") as input_file:
                # input_file.write(f"file '{app.config['UPLOAD_FOLDER']}/{recive_id}/{file}.jpg/'\nduration 1 \n")
                input_file.write(f"file '{file}.jpg'\n")
                input_file.write("duration 3\n")

            print("Uploaded file:", file)

        return "File uploaded successfully"

    return render_template("create.html", my_id=my_id)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)