from flask import Flask, render_template, request
# from aws import upload_file
# from flask import Flask, render_template
# import os

# app = Flask(__name__)

# print("Current Working Directory:", os.getcwd())
# print("Template Folder:", app.template_folder)
# print("Templates Exists:", os.path.exists("templates"))

# # Secret Key
# app.secret_key = "your_secret_key"

# # Home Page
# @app.route("/")
# def home():
#     return render_template("index.html")

# # Register Page
# @app.route("/register")
# def register():
#     return render_template("register.html")

# # Login Page
# @app.route("/login")
# def login():
#     return render_template("login.html")

# # Dashboard Page
# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html")

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import request
# from aws import upload_file
# @app.route("/upload", methods=["POST"])
# def upload():
#     file = request.files["file"]

#     if file:
#         url = upload_file(file, file.filename)
#         return f"Uploaded Successfully: {url}"

#     return "No file selected"
# @app.route("/upload", methods=["POST"])
# def upload():
#     ...
# @app.route("/upload", methods=["POST"])
# def upload():

#     if "file" not in request.files:
#         return "No file selected."

#     file = request.files["file"]

#     if file.filename == "":
#         return "Please choose a file."

#     file_url = upload_file(file, file.filename)

    # return f"File uploaded successfully!<br><br>File URL: {file_url}from flask import Flask, render_template, request
from aws import upload_file
import os

app = Flask(__name__)

print("Current Working Directory:", os.getcwd())
print("Template Folder:", app.template_folder)
print("Templates Exists:", os.path.exists("templates"))

app.secret_key = "your_secret_key"

# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")

# ---------------- REGISTER ----------------

@app.route("/register")
def register():
    return render_template("register.html")

# ---------------- LOGIN ----------------

@app.route("/login")
def login():
    return render_template("login.html")

# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ---------------- UPLOAD ----------------

@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return "No file selected"

    file = request.files["file"]

    if file.filename == "":
        return "Please choose a file"

    url = upload_file(file, file.filename)

    if url:
        return f"""
        <h2>Upload Successful ✅</h2>
        <p>{url}</p>
        """

    return "Upload Failed"

# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)