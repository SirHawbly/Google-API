# modified from google devs.
# # https://developers.google.com/calendar/create-events
 
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


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


COLORS = {
           "blue"      : 1,
           "green"     : 2,
           "purple"    : 3,
           "red"       : 4,
           "yellow"    : 5,
           "orange"    : 6,
           "turquoise" : 7,
           "gray"      : 8,
         }

# 2018-12-07T14:00:00-08:00 Hiss
# 2018-12-14T08:30:00-08:00
def create_event_time(json_time):

	# load the json obj, and index the
	# contents with variables
  json_obj = json.loads(json_time)
  yr  = json_obj['year'] 
  mth = json_obj['month']
  day = json_obj['day']
  hr  = json_obj['hour']
  mi  = json_obj['minute']
  tz  = json_obj['timezone']

  time_string = ""
  time_string += str(yr) + '-'

	# pull in the other fields, adding 0 padding 
	# when needed
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

	# return string
  return time_string


def main(json_event):

  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """

	# grab the json token, and get credentials
  store = file.Storage('token.json')
  creds = store.get()

	# if we dont have credentials we need to 
	# request them
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

  # summary, location, description, start_json, end_json, attendees)
  event_obj = json.loads(json_event)
  start_time = event_obj["start"]
  end_time = event_obj['end']

	# create an event using the provided fields
	# summary, location, desc, start/end time, 
	# reminders, and colorId
  event = {
    'summary': event_obj['summary'],
    'location': event_obj['location'],
    'description': event_obj['description'],
    'start': {
      'dateTime': create_event_time(start_time),
      'timeZone': 'America/Los_Angeles',
    },
    'end': {
      'dateTime': create_event_time(end_time),
      'timeZone': 'America/Los_Angeles',
    },
    'reminders': {
      'useDefault': True,
    },
		'colorId' : COLORS[event_obj['color']]
  }

  event = service.events().insert(calendarId='primary', body=event).execute()
  print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':

	# make some json obj to pass in
  summary = 'adsfsummary'
  location = 'herern'
  description = 'vgooddescription'
  s1 = {"year":2018, "month":11, "day":18, "hour":19, "minute":30, "timezone":8}
  s2 = {"year":2018, "month":11, "day":18, "hour":21, "minute":30, "timezone":8}

  string = {}
  string["summary"] = summary
  string["location"] = location
  string["description"] = description
  string["start"] = json.dumps(s1)
  string["end"] = json.dumps(s2)
  string["color"] = 'blue'

  print(json.dumps(string))

  main(json.dumps(string))

