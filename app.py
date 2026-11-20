from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/schemes")
def schemes():
    return render_template("schemes.html")


@app.route("/eligibility")
def eligibility():
    return render_template("eligibility.html")


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


@app.route("/guidance")
def guidance():
    return render_template("guide.html")


if __name__ == "__main__":
    app.run(debug=True)