""" datetime module - basic date and time types

dir(datetime) - to see what's inside this module
help(datetime.date) - always goot to see before using a new class"""

import datetime     

# datetime - module
# datetime - class
# today() - method

today = datetime.date.today()
print("{:%d, %b %Y} was a great dayl".format(today))  # 25, Oct 2021 was a great day!

# datetime.date() class:
a = datetime.date.today()                  # Returns an object of today's date    
print('datetime.date.today() =', a)
aa = datetime.date(1956, 1, 31)            # Creating a date object
print('datetime.date(1956, 1, 31) =', aa)
print(aa.year)                             # Can access year, month and date separately
print(aa.month)
print(aa.day)
print()

# datetime.timedelta() class:              # Creates an object of length of time
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)               # Object of 100 years
print(mill + dt)
print()

# datetime.datetime() class:
b = datetime.datetime.today()              # Returns an object of today's date and current time
print('datetime.datetime.today() =', b)    
c = datetime.datetime.now()                # Returns an object of today's date and current time
print('datetime.datetime.now() =', c)     
print('separately:', c.year, c.month, c.day, c.hour, c.minute, c.second, c.microsecond)
print()

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)
print() 

# .srtftime() method - string format time. Date formatting: 
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print('The current date is:', datetime.datetime.strftime(a, '%d/%m/%Y'))  # One method
print('The current date is:', a.strftime('%A, %B, %d, %Y'))               # Another way 
print('The current time is:', datetime.datetime.strftime(b, '%H:%M:%S'))
message = "GVR was born on {:%A, %B, %d, %Y}."
print(message.format(aa))                  # aa - is on what object the 'message' format will be applied
print()

# .strptime() method - string parse time. Converts a string into date object:
moon_landing = '7/20/1969'
moon_landing_datetime = datetime.datetime.strptime(moon_landing, '%m/%d/%Y')
print('moon_landing_datetime =', moon_landing_datetime)

