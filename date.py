import datetime as d
from datetime import date

todays = d.datetime(day=7,month=9,year=2018, hour=14, minute=30)

print(d.datetime.today() - todays)
