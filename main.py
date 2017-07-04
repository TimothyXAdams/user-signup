from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/welcome", methods=['POST'])
def welcome():
    return ("Welcome, ", username)



@app.route("/chkform", methods=['POST'])
def chkform():
    error = "" #initialize error as empty string

    username = request.form["username"]
    if len(username) <3 or len(username) > 20:
    	error = "You must enter a valid user name"

    password  =request.form["password"]
    if len(password) <3 or len(password) > 20:
    	error = "Invalid password"

    chkpwd = request.form["chkpwd"]
    if chkpwd != password:
    	error = "Password mismatch"

    emailaddr = request.form["emailaddr"]
    if "@" not in emailaddr or "." not in emailaddr:
    	error = "Make sure email address is valid"

    if error:
        return render_template("user_signup_form.html")
    else:
        return render_template("welcome.html", username=username)



@app.route("/")
def index():
    return render_template('user_signup_form.html')


app.run()
