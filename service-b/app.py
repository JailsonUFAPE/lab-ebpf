from flask import Flask
import time
app = Flask(__name__)
@app.route("/")
def hello():
	time.sleep(0.1)
	return "service B"	
app.run(host="0.0.0.0", port=5001,
debug=False )
