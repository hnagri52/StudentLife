import os
import random
import string
from db_helper import DBHelper
from emailClient import sendMail
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)
app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))
print("secret_key:" + app.secret_key)

# ROUTES FOR LANDING/SIGNUP PAGE
@app.route("/", methods=["GET"])
def checkWho():
    if request.method == "GET":
        # get token
        # if token in db redirect to db
        return "--"
        # else send to homepage

@app.route("/home", methods=["GET"])
@app.route("/home/", methods=["GET"])
def homePage():
    return render_template("index.html")


# ROUTE FOR SIGNUP FORM - POST
@app.route("/signUp", methods=["POST"])
# @app.route("/signUp/", methods=["POST"])
def signUpForm():
    if request.method == "POST":
        body = request.form
        # print(body) # JSON {body: "fname":""...}
        # generating code and urlfor the user account activation
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        # this is where you add the user to the db
        # send a confirmation email
        activationURL = "http://localhost:5000/validate/" + code
        # check for db existance
        if not os.path.exists("studentfile.db"):
            DBHelper().create_db_tables("studentlife")
        # if the db already exists

        message = render_template("email-confirmation.html", url=activationURL)
        sendMail(body["email"], message)
        # once the user is added in the db redirect to dashboard with tokenized cookies
        return jsonify({"body":body})



@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/validate/<code>")
def validateCode(code):
    if DBHelper().activate(code):
        return "activated"
        # return redirect("http://localhost:5000/home", code=302)
    else:
        return "Invalid Code Try again"

@app.route("/email")
def mailConfirmation():
    code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    activationURL = "http://localhost:5000/validate/" + code
    return render_template("email-confirmation.html", url=activationURL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)