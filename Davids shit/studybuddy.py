# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:45:02 2019

@author: gilld
"""

#from forms import ContactForm    
import os
from flask import Flask, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'development key'




@app.route("/user/<username>/study", methods=["GET"])
def studyPage(username):
    #alow saving your school schedule
    #type and recomend courses as u do
    return render_template("study.html")



#test routes below my core function is above
@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

'''
with app.test_request_context(): # this finds the url with for those words and extracts them if that is something you need to access
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
'''



if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8000", debug=False)