""" from datetime import date
import smtplib
import datetime

#Your BT passwords don't need to be changed

Google = datetime.date(2020,9)
Facebook=datetime.datetime(2020,9)
Microsoft=date(2020,9)
SBI=datetime.datetime(2020,9)
TCS=datetime.datetime(2020,9)
print(TCS)


def send_mail(x):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('vermapankaj1997@gmail.com','htfwxstbiripexup')

    subject = 'Change your Passwords now'
   
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'vermapankaj1997@gmail.com',
        'vermapankaj1997@gmail.com',
        msg
    )
    server.quit() """
from flask import Flask, render_template
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route('/')

def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)