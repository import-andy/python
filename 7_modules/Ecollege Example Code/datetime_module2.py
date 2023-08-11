# *** datetime ***

import datetime

today_with_time = datetime.datetime.today()
print(type(today_with_time), today_with_time)

today_without_time = datetime.date.today()
print(type(today_without_time), today_without_time)

#strftime method returns a string
print('The current date is: ', datetime.datetime.strftime(today_without_time, "%d/%m/%y")) 
print('The current time is: ', datetime.datetime.strftime(today_with_time, "%H:%M:%S"))

# formating %symbol meaning
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print("****")
print(datetime.datetime.strftime(today_with_time, "%x"))
print(datetime.datetime.strftime(today_with_time, "%X"))
print(datetime.datetime.strftime(today_with_time, "%c"))

# ---
# Numbers are used in print statements just for output clarity
print("***")
n = datetime.datetime.now() 
print(1, type(n) )
print(2, datetime.datetime.now() )
print(3, n.date())
print(4, n.time())
print(5, n.year, n.month, n.day, n.hour, n.second, n.microsecond ) 

print(6, n.strftime('%a jfdkslajfds %A %d') )
print(7, n.strftime('%b %B %m') )
