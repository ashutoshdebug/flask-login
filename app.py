from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)

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

"""