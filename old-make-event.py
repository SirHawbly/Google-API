# https://developers.google.com/calendar/create-events

# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json


def parse_json_event(json_string):
  # summary location start end
  json_obj = json.loads(json_string)
  return json_obj


def create_event_time(yr, mth, day, hr, mi, tz):
  # 2018-12-07T14:00:00-08:00 Hiss
  # 2018-12-14T08:30:00-08:00
  time_string = ""
  time_string += str(yr) + '-'

  if(mth < 10): time_string += '0' + str(mth) + '-'
  else:  			  time_string +=			 str(mth) + '-'

  if(day < 10): time_string += '0' + str(day) + 'T'
  else:					time_string += 			 str(day) + 'T'
	
  if(hr < 10):  time_string += '0' + str(hr) + ':'
  else:					time_string += 			 str(hr) + ':'

  if(mi < 10):  time_string += '0' + str(mi) + ':00-'
  else:					time_string += 			 str(mi) + ':00-'

  if(tz < 10):  time_string += '0' + str(tz) + ':00'
  else: 				time_string += 			 str(tz) + ':00'

  return time_string


s1 = '{"year":2018, "month":1, "day":4, "hour":8, "minute":3, "timezone":8}' 
s2 = '{"year":2018, "month":12, "day":14, "hour":18, "minute":30, "timezone":10}' 
x1 = json.loads(s1)
x2 = json.loads(s2)
x1 = create_event_time(x1['year'], x1['month'], x1['day'], x1['hour'], x1['minute'], x1['timezone'])
x2 = create_event_time(x2['year'], x2['month'], x2['day'], x2['hour'], x2['minute'], x2['timezone'])
print(x1) 
print(x2) 
assert(False)


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  store = file.Storage('token.json')
  creds = store.get()
  if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('cal-client-cred.json', SCOPES)
    creds = tools.run_flow(flow, store)
  service = build('calendar', 'v3', http=creds.authorize(Http()))

  # Create an httplib2.Http object to handle our HTTP requests, and authorize 
	  # it using credentials.authorize()
  http = Http()

  # http is the authorized httplib2.Http() 
    # or: http = credentials.authorize(httplib2.Http())
  http = creds.authorize(http)        

  service = build('calendar', 'v3', http=creds.authorize(Http()))

  event = {
    'summary': 'Google I/O 2018',
    'location': '800 Howard St., San Francisco, CA 94103',
    'description': 'A chance to hear more about Google\'s developer products.',
    'start': {
      'dateTime': '2018-10-10T09:00:00-07:00',
      'timeZone': 'America/Los_Angeles',
    },
    'end': {
      'dateTime': '2018-10-10T17:00:00-07:00',
      'timeZone': 'America/Los_Angeles',
    },
    'recurrence': [
      'RRULE:FREQ=DAILY;COUNT=2'
    ],
    'attendees': [
      {'email': 'lpage@example.com'},
      {'email': 'sbrin@example.com'},
    ],
    'reminders': {
      'useDefault': False,
      'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
      ],
    },
  }
 
  event = service.events().insert(calendarId='primary', body=event).execute()
  print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':
    main()

