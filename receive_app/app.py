from flask import Flask, jsonify
import requests
import lxml.html

app = Flask(__name__)

@app.route("/api/<url>",methods=["GET","POST"])
def api(url):
    url = "https://"+url
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    print html.xpath("//a/@href")
    return jsonify({"data":html.xpath("//a/@href")})
    

app.run(
    debug=True,
    port=5001
)
