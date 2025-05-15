from flask import Flask,url_for,redirect,request,render_template
import os
import PasswordEncoder as pe
import pickle_loader as pl



app = Flask(__name__)
app.secret_key = "dukee_secret_key_||_key_secret_dukee"

#databse logic

database = 'tenzon_database.db'
if not os.path.exists(database):
    pl.save_pickle({"users":{}},database)
db = pl.load_pickle(database)

app.route("/tenzon/login", methods=["POST","GET"])
def login_user(username,password):
    global db,database
    email = request.form.get("username")
    password = request.form.get("password")
    enoded_password = pe.enoded_password(password)
    for email, attr in db["users"].items():

@app.route("/")
def login():
    return render_template("tenzon/login.html")

@app.route("/signup/form")
def signup_form():
    return render_template("tenzon/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9090)





