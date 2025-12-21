python
import requests
import time

while True:
    try:
        requests.get("http://localhost:5001")
    except:
        pass
    time.sleep(1)
