
import sqlite3, os
from flask import Flask, redirect, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash , check_password_hash

app = Flask(__name__)



#   CONFIGURING THE SECRET KEY 
app.config['SECRET_KEY']=os.urandom(24)

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
    user = None
    if 'user' in session:
        user = session['user']
    return render_template("index.html", user = user)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


#######################################################
###################   LOGIN ROUTE  ####################
#######################################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['email']
        password = request.form['password']

        #   Creating a connection cursor
        user_cur = db.connection.cursor()

         #   select the user from the database
        user_cur.execute("SELECT OwnerID, Email, Pass FROM car_owner WHERE Email= %s", [username])

        #   fetch the user
        logged_user = user_cur.fetchone()

        #   check if the password entered match with the password in the database
        if check_password_hash(logged_user[2], password):

            #   create a session
            session['user'] = logged_user[0]

            return redirect(url_for('home'))
        else:
            return f'<h1>The password is wrong</h1>'

    return render_template('login.html')


#######################################################
################   REGISTER ROUTE  ####################
#######################################################
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        FName = request.form['FName']
        LName = request.form['LName']
        email = request.form['email']
        phone = request.form['phone']
        hashed_pass = generate_password_hash(request.form['password'], method='sha256')
        conf_hashed_pass = generate_password_hash(request.form['conf_password'], method='sha256')

        #   Creating a connection cursor
        user_cur = db.connection.cursor()

        #   Executing SQL Statements
        user_cur.execute("INSERT INTO car_owner (FName, LName, Email, Tel, Pass, Conf_pass)\
                        VALUES (%s, %s, %s, %s, %s, %s)", (FName, LName, email, phone, hashed_pass, conf_hashed_pass))

        #   Saving the actions performed on the DB
        db.connection.commit()
        
        #   Closing the cursor
        user_cur.close()

        return redirect(url_for('login'))


    return render_template('register.html')

######################################################################

@app.route('/accidentAdvices')
def accidentAdvices():
    return render_template('accidentAdvices.html')


@app.route('/maintenanceTips')
def tips():
    return render_template('carmaintenancetips.html')

#######################################################
#################  BOOK SERVICE ROUTE  ################
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
        cursor.execute("INSERT INTO vehicle (Manufacturer, Model, RegYear, Reg_number)\
                        VALUES (%s, %s, %s, %s)", (Manufacturer, Model, RegYear, Reg_number))

        #   Saving the actions performed on the DB
        db.connection.commit()
        
        #   Closing the cursor
        cursor.close()

    return render_template('bookservice.html')


@app.route('/help')
def helpPage():
    return render_template('askforhelp.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


if __name__=="__main__":
    app.run(debug=True)