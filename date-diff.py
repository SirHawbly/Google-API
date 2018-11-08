import datetime as d

todays = d.datetime(day=7,month=9,year=2018, hour=14, minute=30)

def get_remain_days(hr, mn, dy, mnth, yr):
	event_day = d.datetime(hour=hr, minute=mn, day=dy, month=mnth, year=yr)
	return event_day - d.datetime.today()

diff = get_remain_days(14,30,13,8,2019)

print(diff.days)
