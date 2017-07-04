from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


# @app.route("/welcome", methods=['POST'])
# def welcome():
#     return ("Welcome, ", username)



@app.route("/chkform", methods=['POST'])
def chkform():
    username_error = "" #initialize error as empty string
    password_error = ""
    chkpwd_error   = ""
    email_error    = ""

    username = request.form["username"]
    if len(username) <3 or len(username) > 20:
    	username_error = "You must enter a valid user name"

    password  =request.form["password"]
    if len(password) <3 or len(password) > 20:
    	password_error = "Invalid password"

    chkpwd = request.form["chkpwd"]
    if chkpwd != password:
    	chkpwd_error = "Password mismatch"

    emailaddr = request.form["emailaddr"]
    if emailaddr: #If it's not empty, since it's optional
        if " " in emailaddr:
            email_error = "Make sure email address is valid"
        if len(emailaddr) < 3 or len(emailaddr) >20:
            email_error = "Make sure email address is valid"
        if "@" not in emailaddr or "." not in emailaddr:
            email_error = "Make sure email address is valid"

    if username_error or password_error or chkpwd_error or email_error:
        return render_template("user_signup_form.html", username_error=username_error, password_error=password_error, chkpwd_error=chkpwd_error, email_error=email_error, username=username, password=password, emailaddr=emailaddr)
    else:
        return render_template("welcome.html", username=username)



@app.route("/")
def index():
    return render_template('user_signup_form.html')


app.run()
