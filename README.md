# google-cal-daily-events
Simple Python GUI tool to display daily Google calendar
events using the Google Calendar API.

## Requirements
- Python 3.8
- Python Package Installer (Pip)
- A graphical desktop

## About
I use this Google Calendar code in a personal smart alarm
of mine (which is a bit too hackish to redistribute). I
figured it may be useful in other projects. It does just
get the current day's events because that is all I wanted
but you could easily write some additional functions to
get calendar events in specific time periods.

## Setup
Follow the steps below to get setup.

### 1) Get a client secret for the API
See the Google Developer link, (https://developers.google.com/calendar/quickstart/python).
You only need to follow the first step. After you have downloaded the "credentials.json"
file, replace the empty JSON file in (calendar_utils/client_token/credentials.json). Leave
the ".pkl" file.

### 2) Setup the virtualenv
Create a virtual environment. This command will be slightly
different per OS but on Debian-base distros it is:

        python3 -m venv venv

Activate it:
        
        source venv/bin/activate

Install the requirements:

        pip3 install -r pip3-requirements.txt

### 3) Test the program
Run the test.py module:

        python3 test.py

Google will provide a URL for you to copy and paste in your web browser.
You will then sign into your Google account on the resulting page and allow
the app to access your calendar. Finally copy the string that Google provides
and paste it where prompted in the console.

After you have given the program access to your calendar, Enter one of your
calendar IDs where prompted. If you have any events in the calendar on the
current date they will be displayed one-by-one in a graphical window.