from opencivicdata.api import OCDAPI
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lookup", methods=["POST"])
def lookup():
    return render_template("lookup.html")


if __name__ == "__main__":
    app.run(debug=True)
