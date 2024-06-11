#program to go to a specific day in a date
from datetime import datetime
from dateutil.relativedelta import relativedelta
today = datetime.now()
print(today)#18-5-2024

print('---take this date variable to the first day of this month---')
first_day = today + relativedelta(day=1)
print(first_day)
print('----- take this date variable to the last day of this month--')
last_day = today + relativedelta(day=31)
print(last_day)
