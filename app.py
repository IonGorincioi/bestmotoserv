import sqlite3, os
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

##########################################
#####   DATABASE CONFIGURATIONS    #######
##########################################
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Gsandanat.1'
app.config['MYSQL_DB'] = 'GarageDB'
 

db = MySQL(app)

##########################################

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

#########################################
########### REGISTRTATION PAGE ##########
#########################################
@app.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/accidentAdvices')
def accidentAdvices():
    return render_template('accidentAdvices.html')


@app.route('/maintenanceTips')
def tips():
    return render_template('carmaintenancetips.html')

#######################################################
###########   BOOK SERVICE PAGE   #####################
#######################################################
@app.route('/bookService', methods = ['GET', 'POST'])
def bookService():
    if request.method == 'POST':
        carDetails  = request.form
        Manufacturer = carDetails['Manufacturer']
        Model = carDetails['Model']
        RegYear = carDetails['RegYear']
        Reg_number = carDetails['Reg_number']

        #   Creating a connection cursor
        cursor = db.connection.cursor()

        #   Executing SQL Statements
        cursor.execute("INSERT INTO vehicle_service (Manufacturer, Model, RegYear, Reg_number)\
                        VALUES (%s, %s, %s, %s)", (Manufacturer, Model, RegYear, Reg_number))

        #   Saving the actions performed on the DB
        db.connection.commit()
        
        #   Closing the cursor
        cursor.close()

    return render_template('bookservice.html')


@app.route('/help')
def helpPage():
    return render_template('askforhelp.html')


if __name__=="__main__":
    app.run(debug=True)