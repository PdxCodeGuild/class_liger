from datetime import datetime, timedelta
from dateutil import tz

# print(dir(datetime))

now = datetime.now()
# print(now) # 2022-03-16 18:14:40.450997

# POSIX Timestamp time
# print(now.timestamp()) # 1647479762.196428

# ------------------------------------------------------------------------- #

# Datetime at a specific date/time
my_birthday = datetime(year=1988, month=9, day=17, hour=6, minute=32)
# print(my_birthday) # 1988-09-17 06:32:00

# Datetime from a date string
my_birthday = 'September 17, 1988'
my_birthday_datetime = datetime.strptime(my_birthday, "%B %d, %Y")
# print(my_birthday_datetime) # 1988-09-17 00:00:00

# ------------------------------------------------------------------------ #

# Format datetimes into strings
# print(now.strftime("%Y")) # 2022
# print(now.strftime("%B")) # March
# print(now.strftime("%B %d, %Y")) # March 16, 2022
# print(now.strftime("%B %d, %Y %I:%M:%S %p")) # March 16, 2022 # March 16, 2022 06:26:55 PM
# print(now.strftime("%H:%M:%S")) # 18:27:29

# ----------------------------------------------------------------------- #

# Datetime Math

tomorrow = now + timedelta(days=1)
# print(tomorrow) # 2022-03-17 18:29:07.726849

next_year = now + timedelta(days=365)
# print(next_year) # 2023-03-16 18:29:35.978075

the_past = now - timedelta(days=123456)
# print(the_past) # 1684-03-11 18:30:05.249331

# --------------------------------------------------------------------- #

# Timezones
# The 'America/Los_Angeles' or 'Asia/Singapore' strings are unique identifiers
# in the IANA database which tracks ever-changing datetime offsets around the globe
# https://www.iana.org/time-zones

portland_tz = tz.gettz('America/Los_Angeles')
singapore_tz = tz.gettz('Asia/Singapore')

# print(portland_tz.tzname(now), portland_tz.utcoffset(now))
# print(singapore_tz.tzname(now), singapore_tz.utcoffset(now))

# ------------------------------------------------------------------- #