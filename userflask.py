from flask import Flask, render_template, redirect, url_for, flash,request
from flask_mail import Mail, Message
import sqlite3 as sql
app=Flask(__name__)
app.secret_key='random string'
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'anithagk12@gmail.com'
app.config['MAIL_PASSWORD'] = 'anuvinayaga'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
         con=sql.connect("user.db")
         username=request.form['usernm'] 
         password=request.form['pw']         
         cur = con.cursor()
         cur.execute('Select * from userlogin where usernm="%s" and pw="%s"' %(username,password))
         if cur.fetchone() is not None:
            return render_template('record1.html')
         else:
            return "Username or password incorrect"

@app.route('/Register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
       return render_template('collegeregistration.html')
   

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/newuser',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
         usernm = request.form['nm']
         firstname=request.form['ftnm']
         lastname=request.form['ltnm']
         email=request.form['email']
         pw = request.form['pw']
         gender=request.form['gender']
         con=sql.connect("user.db")
         cur = con.cursor()
         cur.execute("INSERT INTO userlogin (usernm,firstname,lastname,email,pw,gender) VALUES (?,?,?,?,?,?)",(usernm,firstname,lastname,email,pw,gender) )
         con.commit()
         con.close()
         msg = Message('Hello', sender = 'anithagk12@gmail.com', recipients = [email])
         msg.body = "You account has been created successfully "
         mail.send(msg)
         return render_template('signin.html')
   

@app.route('/newregi',methods = ['POST', 'GET'])
def addregi():
    if request.method == 'POST':
         firstname = request.form['First_Name']
         lastname=request.form['Last_Name']
         dateofbirth=request.form['date']
         email=request.form['Email']
         mobile=request.form['Mobile']
         gender=request.form['Gender']
         address = request.form['Address']
         city = request.form['City']
         X_percentage = request.form['X_Percentage']
         XII_percentage = request.form['XII_Percentage']
         graduation_percentage = request.form['Graduation_Percentage']
         course=request.form['Course']
         mcourse=request.form['MCourse']
         con=sql.connect("user.db")
         cur = con.cursor()
         cur.execute("INSERT INTO userregist (firstname,lastname,dateofbirth,email,mobile,gender,address,city,X_percentage,XII_percentage,graduation_percentage,course,mcourse) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(firstname,lastname,dateofbirth,email,mobile,gender,address,city,X_percentage,XII_percentage,graduation_percentage,course,mcourse) )
         con.commit()
         con.close()
         msg = Message('', sender = 'anithagk12@gmail.com', recipients = [email])
         msg.body = "Thanks for the Submission "
         mail.send(msg)
         return render_template('record.html')

@app.route('/listone',methods = ['POST', 'GET'])
def listone():
  if request.method == 'POST':
    con = sql.connect("user.db")
    cur = con.cursor()
    cur.execute("select * from userregist order by X_percentage desc, XII_percentage desc")
    datas=cur.fetchall()
    return render_template('test.html',datas=datas)


if __name__ == '__main__':
   app.run(debug = True)
