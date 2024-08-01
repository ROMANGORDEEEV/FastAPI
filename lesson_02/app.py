from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/setcookie", methods=["POST"])
def setcookie():
    user = request.form["nm"]
    email = request.form["email"]
    resp = make_response(redirect(url_for("greeting")))
    resp.set_cookie("userName", user)
    resp.set_cookie("userEmail", email)
    return resp


@app.route("/greeting")
def greeting():
    user = request.cookies.get("userName")
    email = request.cookies.get("userEmail")
    if not user or not email:
        return redirect(url_for("index"))
    return render_template("greeting.html", user=user)


@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie("userName", "", expires=0)
    resp.set_cookie("userEmail", "", expires=0)
    return resp


if __name__ == "__main__":
    app.run(debug=True)
