import random
import http.client
import json
from urllib.parse import quote

nba_data = []


# Initialize jokes
def initNba():
    nba_data = []
        
# Return nba_data from external api


def getNbaAPIData(nba):
    conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")
    payload = ''
    headers = {}
    encodednba = quote(nba)
    conn.request("GET", "/v2/current.json?key=943e1ad914msh028ea477fd00782p17daa1jsn5d479dac7106&q=" + encodednba +"&aqi=no", payload, headers)
    res = conn.getresponse()
    data = res.read()
    decodedString = data.decode("utf-8")
    j = json.loads(decodedString)
    nbaIcon_url = ""
    j['firstname']['lastname'] = nbaIcon_url
    return j

# Test Joke Model
if __name__ == "__main__": 
    initNba()  # initialize jokes
    