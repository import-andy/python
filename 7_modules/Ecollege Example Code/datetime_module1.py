'''Working with basic dates and times using datetime module'''

# objects available in standard __main__ namespace:
print(dir())
print()

# classes and functions for working with dates and times are in the datetime module which must be imported
import datetime

# you can see all the objects available

print(dir(datetime))


print("date, time, and datetime are classes.  Instances (objects) of these classes represent a particular date, time or combination of both\n")

print(datetime.date, '- is used to store and work with dates')

print(datetime.time, '- is used to store and work with time')

print(datetime.datetime, '- a combination of datetime.date and datetime.time')

print(datetime.timedelta, '- A timedelta object represents a duration, the difference between two dates or times.')

print()
print("The most important thing for the MTA Python exam is to be able to: "\
      "\n * parse a string to create coresponding time date and datetime objects from it"\
      "\n * to use those objects to display dates and times in various formats")
