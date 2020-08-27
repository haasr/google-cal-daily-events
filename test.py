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
    for ev in todays_events:
        print('____________________')
        print('Title: '+ ev.title)
        print('Descr: ' + ev.description)
        print('Time:  ' + ev.event_time)
        events.EventWindow(ev)
except:
    print('No events today.')