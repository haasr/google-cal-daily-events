from calendar_utils import cal, events

# Load credentials from your client secret (or pickle file):
cal.load_credentials()

# Get the ids of your calendars:
ids = cal.get_calendar_ids()
print('Your calendar IDs:')
for id in ids:
    print(id)

# Take ID input:
print('Input calendar\'s ID to view its daily events')
id = input('ID >> ')

# Display calendar's daily events one by one:
todays_events = cal.get_events(id)
try:
    print('EVENTS:')
    for ev in todays_events.keys():
        ev_descr = todays_events[ev]
        print(ev_descr)
        events.EventWindow(ev)
except Exception as e:
    print(e)
    print('No events today.')
