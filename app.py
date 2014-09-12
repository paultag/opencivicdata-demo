from opencivicdata.api import OCDAPI
from flask import Flask, render_template, request

app = Flask(__name__)
api = OCDAPI(host="http://10.42.2.102")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lookup", methods=["POST"])
def lookup():
    lat, lon = [request.form[x] for x in ['lat', 'lon']]
    print(lat, lon)
    legs = api.people(lat=lat, lon=lon, fields=",".join([
        "name",
        "memberships.organization.name",
        "memberships.organization.classification",
        "memberships.label",
        "memberships.post.label",
        "memberships.post.role",
    ]))
    return render_template("lookup.html", legs=legs)


if __name__ == "__main__":
    app.run(debug=True)
