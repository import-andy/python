from datetime import date
from datetime import time
from datetime import datetime

# from datetime import date, time, datetime

invoice_date = date.today();
print(invoice_date)
print(datetime.now())

halloween = date(2018, 10, 31) # date function/constructor 
print(halloween)

break_time = time(10, 45, 15) # time function/constructor 
end_time = time(16, 15, 10)

print("Break", break_time)
print("Go Home", end_time)

appointment = datetime(2018, 1, 10, 10, 30, 45, 12345) # datetime function/constructor
print("Python Exam", appointment)


#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
paddys_day = datetime.strptime("3/17/2018", "%m/%d/%Y")
print(paddys_day )

paddys_day = datetime.strptime("17-3-2018", "%d-%m-%Y")
print(paddys_day )

paddys_day = datetime.strptime("2018-3-17", "%Y-%m-%d")
print(paddys_day )

paddys_day = datetime.strptime("03/17/2018 13:45", "%m/%d/%Y %H:%M")
print(paddys_day )

date_str = input("Enter Date of Birth (DD/MM/YYYY): " )
birth_date = datetime.strptime(date_str, "%d/%m/%Y")
print("Original Date Format ", birth_date)

print(birth_date.strftime("%Y-%m-%d"))
print(birth_date.strftime("%m/%d/%Y"))
print(birth_date.strftime("%m/%d/%y"))
print(birth_date.strftime("%b %d, %y"))
print(birth_date.strftime("%B %d, %Y (%A)"))

april_fools = datetime(2018, 4, 1, 13, 00)

print(april_fools.strftime("%B %d, %Y (%A) %H:%M") )
print(april_fools.strftime("%B %d, %Y (%A) %I:%M %p") )
print(april_fools.strftime("%c") )
print(april_fools.strftime("Date %x") )
print(april_fools.strftime("Time %X") )
