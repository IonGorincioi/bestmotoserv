import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/accidentAdvices')
def accidentAdvices():
    return render_template('accidentAdvices.html')


@app.route('/maintenanceTips')
def tips():
    return render_template('carmaintenancetips.html')


@app.route('/bookService')
def bookService():
    return render_template('bookservice.html')


@app.route('/help')
def helpPage():
    return render_template('askforhelp.html')


if __name__=="__main__":
    app.run(debug=True)