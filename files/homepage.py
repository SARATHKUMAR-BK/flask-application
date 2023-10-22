from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import mysql.connector,os
 
app = Flask(__name__)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'root123456'
#app.config['MYSQL_DB'] = 'user'


def dbconnection():
    try:
       db_config = {}
       db_config['host']=os.environ.get("MYSQL_HOST")
       db_config['user']=os.environ.get("MYSQL_USER")
       db_config['password']=os.environ.get("MYSQL_PASSWORD")
       db_config['database']=os.environ.get("MYSQL_DATABASE")
       print(f"dncong: {db_config}")
       db_connection = mysql.connector.connect(**db_config)
       print("Connected to MySQL localhost")
       return db_connection
    except Exception as e:
        print("Db connection failed")
        print(f"Error: {e}")
        return False

def user_validation(user,password):
    try:
      mysql_connection_instance=dbconnection()
      mysql_connection=mysql_connection_instance.cursor()
      if mysql_connection:
          mysql_connection.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, password))
          user=mysql_connection.fetchone()
          print(f"user: {user}")
          mysql_connection.close()
          print("Connection closed")
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    if user:
        return True
    else:
      return False

def add_user(user,password):
    mysql_connection_instance=dbconnection()
    try:
      mysql_connection=mysql_connection_instance.cursor()
      if mysql_connection:
          mysql_connection.execute("INSERT INTO users (username,password) VALUES (%s,%s)", (user, password))
          mysql_connection_instance.commit()
          mysql_connection.close()
          print("Connection closed")
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html')


@app.get('/login')
def login_get():
    return render_template('login.html')

@app.post('/login')
def login_post():
    if user_validation(user=request.form['username'],password=request.form['password']): 
        print(f" username: {request.form['username']}")
        print(request.form['password'])
        print(request.form)
        return redirect(url_for('homepage'))
    else:
        return "<h1> login Failed</h1><br><h1> Pls relogin :<a href=\"/login\">Login Link</a></h1>"

@app.get('/sign-up')
def signup_get():
    return render_template('signup.html')

@app.post('/sign-up')
def signup_post():
    # checking if password and confirm password
    if request.form['password'] == request.form['confirm_password']:
        print("both password and confirm_password are same")
        if add_user(user=request.form['username'],password=request.form['password']):
            return "<h1> Signup success</h1>"
        else:
            return "<h1> Signup not success ,you may login now : <a href=\"/login\">Login Link</a></h1>"
    else:
        return "<h1> password and confirm_password are mismatching </h1><br><h1> Pls signup again :<a href=\"/sign-up\">sign-up Link</a></h1>"


@app.route('/application/')
def homepage():
    return "<h1> sarath application </h1>"
