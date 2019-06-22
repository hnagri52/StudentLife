# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:24:30 2019

conf email script

@author: gilld
"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#class Email(object):
def send_email(receiver_email,recipient):
    port = 465  # For SSL
    sender_email = "studentlifeenghack@gmail.com"
    password = "!studentlife1"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Create the plain-text and HTML version of your message
    text = """\
    Hi """+recipient +""",
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.realpython.com">Real Python</a> 
           has many great tutorials.
        </p>
      </body>
    </html>
    """
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        
        server.login(sender_email, password) 
        # TODO: Send email here
       
    
    
        server.sendmail(sender_email, receiver_email, message.as_string())