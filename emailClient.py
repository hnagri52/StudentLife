import smtplib
from email.mime.text import MIMEText

def sendMail(recpient, msg):
    title = 'Hackmeet Acount Confirmation'
    message = MIMEText(msg, 'html')

    message['From'] = "studentlifeenghack@gmail.com"
    message['To'] = recpient
    message['Subject'] = title

    msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587') # SMTP server settings
    server.starttls() # asking the google server for permission to connect
    server.login("studentlifeenghack@gmail.com", '!studentlife1') # login credentials
    server.sendmail("studentlifeenghack@gmail.com", recpient, msg_full) # sending email
    server.quit() # disconneting from the user