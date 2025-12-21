from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def call():
    r = requests.get("http://service-b:5001")
    return "Service A -> " + r.text

app.run(host="0.0.0.0", port=5000, 
debug=False)
