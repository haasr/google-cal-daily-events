from datetime import datetime, timedelta
from calendar_utils.events import Event
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pkg_resources
import pickle
import os

ACCESS_SCOPES = ['https://www.googleapis.com/auth/calendar']

todays_events = {}

credentials = None
service = None


def clear_events():
    todays_events.clear()


def load_credentials():
    global credentials
    global service
    
    token_path = pkg_resources.resource_filename(__name__, 
                                     '/client_token/token.pkl')
    try:
        credentials = pickle.load(open(token_path,'rb'))
    except:
        flow = InstalledAppFlow.from_client_secrets_file(
                pkg_resources.resource_filename(__name__, 
                                        'client_token/credentials.json'),
                                        scopes=ACCESS_SCOPES)

        credentials = flow.run_console()
        pickle.dump(credentials, open(token_path, 'wb'))
    
    credentials = pickle.load(open(token_path,'rb'))
    service = build('calendar', 'v3', credentials=credentials)


def get_calendar_ids():
    calendar_ids = []
    calendars = service.calendarList().list().execute()
    for cal in calendars['items']:
        calendar_ids.append(cal['id'])
    return calendar_ids


def get_events(calendar_id):
    try:
        # showHiddenInvitations needed to be true to get non-all-day events...
        now = datetime.now().strftime('%Y-%m-%d')
        start = now + 'T00:00:00.00000Z'
        end = ( (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
                + 'T00:00:00.00000Z')
        try:
            events_result = service.events().list(
                                                calendarId=calendar_id,
                                                timeMin=start,
                                                timeMax=end,
                                                showHiddenInvitations=True,
                                                singleEvents=False,
                                                orderBy='startTime',
                                            ).execute()
        except:
            events_result = service.events().list(
                                                calendarId=calendar_id,
                                                timeMin=start,
                                                timeMax=end,
                                                showHiddenInvitations=True,
                                                singleEvents=False,
                                            ).execute()

        events = events_result.get('items', [])

        for event in events:
            try:
                start_date = event['start']['date']
            except:
                start_date = event['start']['dateTime']

            split = start_date.split('-', 1)

            year       = split[0]
            start_date = split[1]

            if ('T' in start_date):
                split = start_date.split('T')
                start_date = split[0]
                time = split[1][:5]
            else:
                time = 'All day'

            if ('summary' in event):
                title = event['summary']
            else:
                title = 'Event'

            if ('description' in event):
                description = event['description']
            else:
                description = ''

            calendar_event = Event(title, start_date, time, description)

            if (time == 'All day'):
                message = ('You have ongoing event '
                            + title + '. ' + description)
            else:
                message = ('At ' + time + ' today, you have event '
                        + title + '. ' + description)

            todays_events[calendar_event] = message

        return todays_events

    except Exception as e:
        print(e)

