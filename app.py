import sqlite3
from flask import Flask, abort, request, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import db
import config
import tests

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    all_tests = tests.get_tests()
    return render_template("index.html", tests=all_tests)

@app.route("/find_test")
def find_test():
    query = request.args.get("query")
    if query:
        results = tests.find_tests(query)
    else:
        query = ""
        results = []
    return render_template("find_test.html", query=query, results=results)

@app.route("/test/<int:test_id>")
def show_test(test_id):
    test = tests.get_test(test_id)
    if not test:
        abort(404)
    return render_template("show_test.html", test=test)

@app.route("/new_test")
def new_test():
    return render_template("new_test.html")

@app.route("/create_test", methods=["POST"])
def create_test():
    aine = request.form["aine"]
    aihe = request.form["aihe"]
    vuosi = request.form["vuosi"]
    koe = request.form["koe"]
    user_id = session["user_id"]

    tests.add_test(aine, aihe, vuosi, koe, user_id)

    return redirect("/")

@app.route("/edit_test/<int:test_id>")
def edit_test(test_id):
    test = tests.get_test(test_id)
    if not test:
        abort(404)
    if test["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_test.html", test=test)

@app.route("/update_test", methods=["POST"])
def update_test():
    test_id = request.form["test_id"]
    test = tests.get_test(test_id)
    if not test:
        abort(404)
    if test["user_id"] != session["user_id"]:
        abort(403)
    aine = request.form["aine"]
    aihe = request.form["aihe"]
    vuosi = request.form["vuosi"]
    koe = request.form["koe"]

    tests.update_test(test_id, aine, aihe, vuosi, koe)

    return redirect("/test/" + str(test_id))

@app.route("/remove_test/<int:test_id>", methods=["GET", "POST"])
def remove_test(test_id):
    if request.method == "GET":
        test = tests.get_test(test_id)
        if not test:
            abort(404)
        if test["user_id"] != session["user_id"]:
            abort(403)
        return render_template("remove_test.html", test=test)

    if request.method == "POST":
        if "remove" in request.form:
            tests.remove_test(test_id)
            return redirect("/")
        else:
            return redirect("/test/" + str(test_id))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return render_template("create_user.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
       
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]
        user_id = result["id"]
        password_hash = result["password_hash"] 

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/")

if __name__ == '__main__':
    app.run()
