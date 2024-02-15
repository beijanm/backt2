import requests

def get_eventbrite_events(public_token):
    headers = {
        "Authorization": f"Bearer {public_token}",
    }
    # Replace with the actual Eventbrite API endpoint you wish to use.
    url = "https://www.eventbriteapi.com/v3/events/search/"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        events = response.json().get('events', [])
        
        # Organize events into a 4x5 grid
        grid = []
        for i in range(4):  # 4 rows
            row = []
            for j in range(5):  # 5 columns per row
                index = i * 5 + j
                if index < len(events):
                    event = events[index]
                    row.append({'name': event['name']['text'], 'picture': event.get('logo', {}).get('url', 'No picture available')})
                else:
                    break  # Break if there are fewer events than spaces in the grid
            if row:
                grid.append(row)
        return grid
    else:
        print("Failed to fetch events")
        return []

# Replace 'Z6GK7TDVPBMZJVRCZ2RL' with your public token variable
events_grid = get_eventbrite_events("Z6GK7TDVPBMZJVRCZ2RL")
for row in events_grid:
    print(row)
