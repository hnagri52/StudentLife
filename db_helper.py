import sqlite3 as sql
import uuid

class DBHelper(object):
    # create database and tables: user, hackmeet
    def create_db_tables(self, db_name):

        try:
            con = sql.connect(db_name) # will create db if not exist

            cur = con.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            rows = cur.fetchall()
            
            create_hackmeet = """
            CREATE TABLE "hackmeet" (
            "first_name"    TEXT,
            "last_name" TEXT,
            "school"    TEXT,
            "field" TEXT,
            "coding_langauge"   TEXT,
            "coding_experience" INTEGER
            );"""

            create_user = """
            CREATE TABLE "user" (
            "first_name"    TEXT,
            "last_name" TEXT,
            "email" TEXT,
            "password"  TEXT,
            "active" BOOLEAN,
            "code" TEXT,
            "token" TEXT
            );
            """
            con.execute(create_hackmeet)
            con.execute(create_user)
            con.commit()
            con.close()

            return "SUCCESS"
        except:
            return "Error creating tables."

    # insert new users
    def insert(self, user, code):

        fname = user['fname']
        lname = user['lname']
        email = str(user['email'])
        password = user['password']

        con = sql.connect("studentlife.db")
        sqlstring = "INSERT INTO user(first_name, last_name, email, password, active, code) VALUES ( '%s','%s','%s','%s', 'False', '%s')" % (fname, lname, email, password, code)

        print(sqlstring)
        con.execute(sqlstring)
        con.commit()

        return "SUCCESS"

    # activate user
    def activate(self, code):
        
        con = sql.connect("studentlife.db")
        cur = con.cursor()
        cur.execute("SELECT 1 FROM user WHERE code='%s'" % (code))

        if cur.fetchone() is not None:
            con.execute("UPDATE user SET active = True WHERE code='%s'" % code)
            con.commit()
        
        con.close()

        return True

    # login to website
    def login(self, username, password):

        con = sql.connect("studentlife.db")
        cur = con.cursor()
        cur.execute("SELECT first_name, last_name from user WHERE email='%s' and password='%s'" % (username, password)) 
        acc = cur.fetchone()

        if acc is not None:
            token = str(uuid.uuid4())
            con.execute("UPDATE user SET token = '%s' WHERE email = '%s'" % (token, username))
            con.commit()
        else:
            token = None

        return token

    # get name based on token
    def get_name(self, token):

        con = sql.connect("studentlife.db")
        cur = con.cursor()
        cur.execute("SELECT first_name, last_name from user WHERE token='%s'" % (token))
        acc = cur.fetchone()
        
        return acc