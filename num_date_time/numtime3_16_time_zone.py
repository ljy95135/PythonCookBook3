from datetime import datetime, timedelta
from pytz import timezone, utc

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d, type(loc_d))  # datetime

bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

# summer time: normalize
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)  # can't just add 30 min
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

# always use GMT/UTC and then localize
utc_d = loc_d.astimezone(utc)
print(utc_d)
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

#  pytz.country_timezones to search timezone
