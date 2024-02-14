import random
import http.client
import json
from urllib.parse import quote

import http.client
import json

def initNba():
    global nba_data
    nba_data = []


def getNbaAPIData():
    conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': '943e1ad914msh028ea477fd00782p17daa1jsn5d479dac7106',
        'X-RapidAPI-Host': 'api-nba-v1.p.rapidapi.com'
    }
    # Assuming you want to fetch a list of players, the correct endpoint needs to be used.
    # This is an example endpoint; you need to replace it with the correct one as per the API documentation.

    conn.request("GET", "/players?search=Alex", '', headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))
