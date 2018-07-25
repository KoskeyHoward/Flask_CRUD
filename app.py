from flask import Flask, render_template

from data import Articles
# import mail 
from flask_mail import Mail, Message
#import mysql connector

import mysql.connector
app = Flask(__name__)

#configure mail
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='howardbright2014@gmail.com',
    MAIL_PASSWORD='P@ssword5050')
mail = Mail(app)

#configure database

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "flask")

# define routes
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/blog')
def blog():
    return render_template('blog.html', blog=Articles)


@app.route('/lifestyle')
def lifestyle():
    return render_template('lifestyle.html')


@app.route('/travel')
def travel():
    return render_template('travel.html')


@app.route('/about')
def about():
    return render_template('about.html')


# route for specific article
@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)


# get articles
Articles = Articles()


# start mailing

@app.route('/send-mail')
def send_mail():
    msg = Message("Sending mail Tutorial by HowardKoskey",
                  sender="howardbright2014@gmail.com",
                  recipients=["deborahcherotich@gmail.com"])
    msg.body = "Hi, \n How are you getting along with this Tutorial?"
    mail.send(msg)
    return 'Email Sent successfully '
#create Database

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")


if __name__ == '__main__':
    app.run(debug=True)
