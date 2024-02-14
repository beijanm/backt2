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
    
    
import http.client
import json

def getNbaAPIData():
    conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': '1306b1f63emsha5d59ab521a0ab0p111cd2jsnd07add0e48ff',  # Make sure to replace 'YOUR_API_KEY_HERE' with your actual API key
        'X-RapidAPI-Host': 'api-nba-v1.p.rapidapi.com'
    }
    conn.request("GET", "/players/league/standard", '', headers)  # Adjust the endpoint as necessary
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

# No need for 'if __name__ == "__main__":' block here as it's part of the model
