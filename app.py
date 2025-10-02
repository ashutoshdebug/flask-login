from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret" # It requires as we are dealing with the login system, it locks the session for a user so that only the desired user can access the session

#homepage login page

@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username # store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again", mimetype="text/plain") #mimetype helps to tell the app to send data in which form, by default it sends it in html type, text/plain tells it to send in plain form
    
    return """
<h2>Login Page</h2>
<form method = "POST">
Username: <input type = "text" name = "username"><br />
Password: <input type = "text" name = "password"><br />
<input type = "submit" value = "login">
</form>
"""

# WELCOME page (after login)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2> Welcome, {session["user"]}!</h2>
        <a href = {url_for('logout')}>Logout</a>
'''
    return redirect(url_for("login"))

# logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))