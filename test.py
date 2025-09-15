from flask import Flask, request
app = Flask(__name__) # __name__ points towards our app

@app.route("/")
def home():
    return "Hello"

# @ is decorator

# @app.route("/submit")
# def submit():
#     return "Submit page"


@app.route("/about")
def about():
    return "About page"

# POST method: Helps to send data to the server, for processing by the server
# GET method: You recieve data from the server, you either send very minimal or no data to the server

@app.route("/submit", methods = ["GET", "POST"])
# Always define methods in a list and string form like above , methods = ["GET", "POST"]
def submit():
    if request.method == "POST": # request helps to check which type of method request is asked by the client
        return "You can fill the form"
    else:
        return "You are viewing the form"
    
# response: Data send to the user by the server. Example: request.form["name"] from a form
# redirect: Move user to different page. Example: return Response(......., mimetype = .....)
# url_for: Build a route dynamically from function name. Example: url_for("home") -> "/home". This will help in us by removing the need of hardcoding the url
# session: It remembers the user info across the pages. Example: session["username"] = "ashutosh"hey