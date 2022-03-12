from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/profile", methods=["GET","POST"])
def profile():
    username = request.form["username_field"]
    password = request.form["password_field"]
    return render_template("profile.html", username=username, password=password)

if __name__ == "__main__" :
    app.run(debug=True)