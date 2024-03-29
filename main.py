import os
import uuid
import random
import string
import languages
from db_helper import DBHelper
from emailClient import sendMail
from flask import Flask, render_template, request, jsonify, redirect, make_response, url_for, json

app = Flask(__name__)
app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))
print("secret_key:" + app.secret_key)

# ROUTES FOR LANDING/SIGNUP PAGE
@app.route("/", methods=["GET"])
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
            DBHelper().insert(body, code)

        message = render_template("email-confirmation.html", url=activationURL)
        sendMail(body["email"], message)
        # once the user is added in the db redirect to dashboard with tokenized cookies
        return redirect("http://localhost:5000/login")



@app.route("/dashboard")
def dashboard():
    token = request.cookies.get('token')
    if token:
        acc = DBHelper().get_name(token)
        user = "%s %s" % (acc[0].capitalize(), acc[1].capitalize())
        return render_template("dashboard.html", user=user)
    else:
        return render_template("dashboard.html", user=None)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        body = request.form

        # retrieve account info
        token = DBHelper().login(body["username"], body["password"])

        # if login success
        if token is not None:
            resp = make_response(redirect("http://localhost:5000/dashboard"))
            resp.set_cookie('token', token)
            return resp

        # if login fails
        else:
            return render_template("login.html", login_error=True)

    elif request.method == "GET":
        return render_template("login.html", login_error=False)

@app.route("/api")
@app.route("/api/")
def internalApi():
    return render_template("api_view.html")

@app.route("/api/demo")
def returnDemo():
    return jsonify(languages.extract_languages())

@app.route("/login?activated")
def login_activated(activated):
    return render_template("login_activated.html")

@app.route("/logout")
def logout():
    resp = make_response(render_template("index.html", user=None))
    if request.cookies.get('token'):
        resp.set_cookie('token', '', expires=0)

    return resp

@app.route("/validate/<code>")
def validateCode(code):
    if DBHelper().activate(code):
        # return "activated"
        return render_template("login_activated.html")
    else:
        return "Invalid Code Try again"

@app.route("/email")
def mailConfirmation():
    code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    activationURL = "http://localhost:5000/validate/" + code
    return render_template("email-confirmation.html", url=activationURL)

@app.route("/hackathons")
def hackathons():
    token = request.cookies.get('token')
    user = None
    if token:
        acc = DBHelper().get_name(token)
        user = "%s %s" % (acc[0].capitalize(), acc[1].capitalize())

    # get the json file with hackathons data
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "hackathons.json")
    with open(json_url, encoding='utf-8') as fh:
        data = json.load(fh)['data']

    return render_template("hackathons.html", hackathons=data, user=user)

@app.route("/hackathons/event")
def events():
    token = request.cookies.get('token')
    user = None
    if token:
        acc = DBHelper().get_name(token)
        user = "%s %s" % (acc[0].capitalize(), acc[1].capitalize())

    # get query params
    event_name = request.args.get('event_name', default='EngHack', type = str)

    # get the json file with hackathons data
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "hackathons.json")
    with open(json_url, encoding='utf-8') as fh:
        data = json.load(fh)['data']
        details = [d for d in data if event_name in d['name']]

    if len(details) > 0:
        details = details[0]

    print(details)
    return render_template("event.html", hackathon=details, user=user, event_name=event_name)    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)