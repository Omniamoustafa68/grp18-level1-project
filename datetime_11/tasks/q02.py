print('--Check if a specific date exists in a list of dates--')
from datetime import datetime

given_date = datetime(2023, 8, 15)
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
is_found = False
for i in range(len(dates_list)):
    if given_date == dates_list[i]:
        print(given_date, 'is found in index:', i)
        is_found = True

if not is_found:
    print(given_date, 'is not found in dates_list')
