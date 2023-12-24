import json
from flask import Flask, render_template, request

api = Flask(__name__)
users = []
MY_DATA = 'users.txt'

def load_data():
    global users
    with open(MY_DATA, 'r') as filehandle:
        users = json.load(filehandle) 

def save_2_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(users, filehandle)


@api.route('/')
def hello():
    return render_template("index.html")


@api.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        users.append({"user": user, "pwd": pwd})
        save_2_file()
        return render_template("success.html", welc_user=user)
    return render_template("register.html")


@api.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        load_data()
        for usr in users:
            if user == usr["user"] and pwd == usr["pwd"]:
                return render_template("success.html", welc_user=user)
    return render_template("login.html")


if __name__ == '__main__':
    api.run(debug=True)
