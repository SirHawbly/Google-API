# # modified from google dev
# https://developers.google.com/calendar/quickstart/python 

# # here is the first line
# # this file is for a Google
# # Calendar Bridge

from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime as d

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def parse_json_time(json_obj):
    """
        input:
        '2018-11-18T18:30:00-08:00' 

        output:
        {'y':2018,'t':11,'d':18,'h':18,'m':30}
    """

    t = {}

    # print(json_obj)
    tokens = json_obj.split("T")

	  # pull the first half with the date info
	  # parse it by hyphens
    date_obj = tokens[0].split("-")
    t['y'] = int(date_obj[0])
    t['t'] = int(date_obj[1])
    t['d'] = int(date_obj[2]) 

    # pull the second half of the date 
    # parse it by hyphens then by colons
    time_obj = tokens[1].split("-")
    time_obj = time_obj[0].split(":")
    t['h'] = int(time_obj[0])
    t['m'] = int(time_obj[1])

		# return the dict obj
    print(t)
    return t 


#def get_remain_days(hr, mn, dy, mnth, yr):
def get_remain_days(json_event_time):
    """input:
				{'dateTime': '2018-11-18T18:30:00-08:00', 
        'timeZone': 'America/Los_Angeles'}

			 output:
				time delta from 0:00am today to provided 
				datetime time. (0:00am today -> 6:30pm 11-18-2018)
    """

    # print (json_event_time)
		# pull out the date_time of the json obj
    date_time = json_event_time['dateTime']

    # parse the date_time string and get a dict back
    t = parse_json_time(date_time)
		
		# create a datetime obj with the data from dict
    event_day = d.datetime(hour=t['h'], minute=t['m'], day=t['d'], month=t['t'], year=t['y'])

    # pull the current day
    today = d.datetime.today()

    # convert todays date to be midnight
    today = d.datetime.combine(today, d.datetime.min.time())

    # print(event_day)
    # print(today)
    return event_day - today


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    # grab the users token (has user's access and refresh tokens)
		# if they dont exist then they are created upon autorization
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    # get a HTTP connection to googles calendar
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
				# 2018-11-09T14:00:00-08:00 Hiss
        print(start, event['summary'])
        print (get_remain_days(event['start']).days)


if __name__ == '__main__':
    main()
