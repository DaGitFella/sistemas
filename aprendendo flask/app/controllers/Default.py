from app import app
from flask import redirect, url_for, render_template, request, session, flash

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    email = None
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        email = request.form["mail"]
        session["email"] = email
        session["user"] = user #stores data on a session dictionary
        flash("Login Succesful!")
        flash(f"Welcome, {user}!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        if "email" in session:
            email = session["email"]
        return render_template("login.html")

@app.route('/user,', methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]       
        return render_template('user.html', usr=user)
    else:
        flash("You're now logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session: #checks if user is stored in the session dictionary keys
        user = session["user"]
        flash(f"{user} has logged out sucessfuly!", "info")
    session.pop("user", None) #removes the user key from the session dictionary
    session.pop("email", None)
    return redirect(url_for("login"))