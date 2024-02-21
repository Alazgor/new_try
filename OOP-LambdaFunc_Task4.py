# import datetime
#
# # Sample datetime object
# sample_datetime = datetime.datetime(2020, 1, 15, 9, 3, 32, 744178)
#
# # Using lambda functions to extract year, month, date, and time
# extract_year = lambda dt: dt.year
# extract_month = lambda dt: dt.month
# extract_day = lambda dt: dt.day
# extract_time = lambda dt: dt.strftime("%H:%M:%S.%f")
#
# # Output the sample datetime and its components
# print(sample_datetime)
# print(extract_year(sample_datetime))
# print(extract_month(sample_datetime))
# print(extract_day(sample_datetime))
# print(extract_time(sample_datetime))

import datetime
date_time = datetime.datetime.now()
# print(date_time.strftime("%H:%M:%S"))
(lambda date_time: (print(date_time.strftime("%Y")),
print(date_time.strftime("%m")),
print(date_time.strftime("%d")),
print(date_time.strftime("%H:%M:%S"))))(date_time)