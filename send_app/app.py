from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        url = request.form.get("url")
        r = requests.get("http://localhost:5001/api/"+url)
        print r.raw
        return render_template("index.html",links=json.loads(r.content)["data"])
    return render_template("index.html")

app.run(debug=True)
