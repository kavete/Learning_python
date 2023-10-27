from datetime import date, datetime, timedelta

today = date.today()

print(today)

date_and_time = datetime.now()

print(date_and_time)

formatted_date = today.strftime("%a, %d %B %Y")

print(formatted_date)

ten_days_ago = today - timedelta(days=10)

print(ten_days_ago)

ten_days_ago = ten_days_ago.strftime("%a, %d %B %Y")

print(ten_days_ago)


#  Assignment

# date_string = "2023-10-27"

# date_object = datetime.strptime(date_string, "%Y-%m-%d")
# print(date_object)


#  Covert a string to a date object
random_date = "2023-10-7 09:22:54"

rd_formatted = datetime.strptime(random_date, "%Y-%m-%d %H:%M:%S")

print(rd_formatted)

date_only = rd_formatted.strftime("%d-%M-%Y")

print(date_only)

# some_date = "2021-12-23"
# object_format = datetime.strptime(some_date, "%Y-%M-%d")

# print(object_format)


# Get difference between 2 dates

date1 = "2019/7/10"
date2 = "2023-5-12"

date1 = datetime.strptime(date1, "%Y/%m/%d")
date2 = datetime.strptime(date2, "%Y-%m-%d")

if date1 > date2:
    difference = date1 - date2
else:
    difference = date2 - date1

print(difference)
