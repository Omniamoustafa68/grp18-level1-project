#program to show the nearest sundays
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
today = datetime.now()

print('---- find the nearest sunday from today---')# 19 - 5 - 2024
nearest_sunday = today + relativedelta(weekday=calendar.SUNDAY)#6
print(nearest_sunday)

print('--find the nearest 2nd sunday from today----')#26 - 5 - 2024
nearest_2nd_sunday = today +relativedelta(weekday=calendar.SUNDAY, weeks=1)
print(nearest_2nd_sunday)

print('--find the first sunday from the beginning of the current month---')
first_day_of_month= today + relativedelta(weekday=calendar.SUNDAY, day=1)
print(first_day_of_month)

print('--find the first sunday from the beginning of next month ---')
first_sunday_of_next_month = today + relativedelta(weekday=calendar.SUNDAY,day=1,months=1)
print(first_sunday_of_next_month)

print('---find the first sunday from the beginning of the current year---')
first_sunday_of_year = today + relativedelta(weekday=calendar.SUNDAY,day=1,month=1)
print(first_sunday_of_year)

print('find the first sunday from beginning of next year---')
first_sunday_of_next_year = today + relativedelta(weekday=calendar.SUNDAY, day=1, years=1, month=1)
print(first_sunday_of_next_year)