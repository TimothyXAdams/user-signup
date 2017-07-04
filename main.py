from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/welcome", methods=['POST'])
def welcome():
    return ("Welcome, ", username)



@app.route("/chkform", methods=['POST'])
def chkform():
    error = "" #initialize error as empty string

    if len(username) <3 or len(username) > 20:
    	error = "You must enter a valid user name"
    if len(password) <3 or len(password) > 20:
    	error = "Invalid password"
    if chkpwd != password:
    	error = "Password mismatch"
    if "@" not in emailaddr or "." not in emailaddr:
    	error = "Make sure email address is valid"
    if error:
        return render_template("/", error=error)
    else:
        return render_template("/welcome")



@app.route("/")
def index():
    encoded_error = request.args.get("error")
    error = ""
    return render_template('user_signup_form.html', error=error)
    #return render_template('edit.html', watchlist=get_current_watchlist(), error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
