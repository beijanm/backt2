import requests
import random
import webbrowser
from urllib.parse import quote

# Eventbrite OAuth and API information
CLIENT_ID = '4RDBODX6XBJOVTTCZR'
PUBLIC_TOKEN = 'Z6GK7TDVPBMZJVRCZ2RL'
REDIRECT_URI = 'http://127.0.0.1:4000/RezApp/2024/02/13/App_Hub.html'
AUTHORIZE_URL = f'https://www.eventbrite.com/oauth/authorize?response_type=token&client_id={CLIENT_ID}&redirect_uri={quote(REDIRECT_URI)}'

def open_authorization_url():
    """Open the Eventbrite authorization URL in the default web browser."""
    webbrowser.open(AUTHORIZE_URL)
    print("Authorization URL opened in browser. Please authorize the app.")

def get_random_eventbrite_event():
    """Fetch a random event from Eventbrite."""
    headers = {
        "Authorization": f"Bearer {PUBLIC_TOKEN}",
    }
    url = "https://www.eventbriteapi.com/v3/events/search/"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        events = response.json().get('events', [])
        
        if events:
            random_event = random.choice(events)
            event_details = {
                'name': random_event['name']['text'],
                'picture': random_event.get('logo', {}).get('url', 'No picture available'),
                'description': random_event['description']['text'] if random_event['description'] else "No description available",
                'url': random_event['url']
            }
            return event_details
        else:
            return "No events found."
    else:
        return "Error fetching events."

if __name__ == "__main__":
    # Uncomment the next line to initiate the OAuth flow
    # open_authorization_url()
    
    # Fetch and display a random event
    random_event_details = get_random_eventbrite_event()
    print(random_event_details)
