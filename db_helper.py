import sqlite3 as sql

class DBHelper(object):
    # create database and tables: user, hackmeet
    def create_db_tables(self, db_name):

        try:
            con = sql.connect(db_name) # will create db if not exist

            cur = con.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            rows = cur.fetchall()
            tables = [table['name'] for table in rows]

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
            "code" TEXT
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
        sqlstring = f"INSERT INTO user(first_name, last_name, email, password, active, code) \
            VALUES( '{fname}','{lname}','{email}','{password}',False, '{code}')"

        print(sqlstring)
        con.execute(sqlstring)
        con.commit()

        return "SUCCESS"

    # activate user
    def activate(self, code):
        
        con = sql.connect("studentlife.db")
        cur = con.cursor()
        cur.execute(f"SELECT 1 FROM user WHERE code='{code}'")

        if cur.fetchone() is not None:
            con.execute(f"UPDATE user SET active = True WHERE code='{code}'")
            con.commit()
        
        con.close()

        return

    # login to website
    def login(self, username, password):

        con = sql.connect("studentlife.db")
        cur = con.cursor()
        cur.execute(f"SELECT first_name, last_name from user WHERE email='{username}' and password='{password}'")
        acc = cur.fetchone()

        print(acc)


if __name__ == '__main__':
    dbhelper = DBHelper()
    # dbhelper.create_db_tables('studentlife.db')
    # dbhelper.activate(101)
    # dbhelper.login('jane@ex.com', 'jane')