import os
from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
import db_helper

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
        # print(body) # JSON {body: "fname":""...}

        # add the user to the db
        body = request.form
        fname = body['fname']
        lname = body['lname']
        email = str(body['email'])
        password = body['password']


        con = sql.connect("studentlife.db")
        sqlstring = f"INSERT INTO user(first_name, last_name, email, password, active) VALUES( '{fname}','{lname}','{email}','{password}',False)"
        # print(sqlstring)

        print(sqlstring)
        con.execute(sqlstring)
        con.commit()
        print(f"SUCCESS: {fname}")

        return jsonify({"body":body})

@app.route('/listnames')
def listnames():
   con = sql.connect("studentlife.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from hackmeet")
   
   rows = cur.fetchall();
   res = [f"{row['first_name']} {row['last_name']}" for row in rows]

   return str(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)