import requests
import random

def get_random_eventbrite_event(public_token):
    headers = {
        "Authorization": f"Bearer {public_token}",
    }
    # Replace with the actual Eventbrite API endpoint you wish to use.
    url = "https://www.eventbriteapi.com/v3/events/search/"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        events = response.json().get('events', [])
        
        if events:
            # Select a random event from the list
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
        print("Failed to fetch events")
        return "Error fetching events."

random_event_details = get_random_eventbrite_event("Z6GK7TDVPBMZJVRCZ2RL")
print(random_event_details)
