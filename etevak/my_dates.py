import datetime

some_date = datetime.datetime(2023, 10, 27)

print(some_date.strftime("%B"))

print(some_date.strftime("%A"))

right_now = datetime.datetime.now()

print(right_now.strftime("%A %d %b %Y %H:%M:%S"))
