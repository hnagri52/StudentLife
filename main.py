import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
@app.route("/home/", methods=["GET"])
def homePage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)