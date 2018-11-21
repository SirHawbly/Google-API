from datetime import date, timedelta, datetime

MAX_DAYS = 30
WEEK_DAYS = ['Monday','Tuesday','Wednesday','Thursday',
							'Friday','Saturday','Sunday']

today = datetime.today()
max_delta = timedelta(days=MAX_DAYS)

# --
def get_days():

  days = []

  for i in range(max_delta.days):

    temp_datetime = today + timedelta(i)

    temp_date = {}
    temp_date['day']     = temp_datetime.day
    temp_date['month']   = temp_datetime.month
    temp_date['year']    = temp_datetime.year
    temp_date['weekday'] = temp_datetime.weekday()
    days.append(temp_date)

  return days
# --


cal_days = get_days()
# print (cal_days)


# --
def print_calendar():

  for day in WEEK_DAYS:
    print(' ' + day[0:3] + '  ', end='')
  print()

  day = cal_days[0]
  for i in range(day['weekday']):
    print('      ', end='')
    # print('mm-dd ', end='')

  for day in cal_days:
    print(str(day['month']).zfill(2) + '-' + 
            str(day['day']).zfill(2) + ' ', end='')
    if (day['weekday'] == 6):
       print()
  print()
# --


print_calendar()
