import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
@app.route("/home/", methods=["GET"])
def homePage():
    return render_template("index.html")


@app.route("/signUp", methods=["POST"])
def signUpForm():
    if request.method == "POST":
        body = request.form
        print(body) # JSON {body: "fname":""...}
        # this is where you add the user to the db
        return jsonify({"body":body})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)