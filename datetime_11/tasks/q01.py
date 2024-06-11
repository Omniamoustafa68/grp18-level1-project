print('---Find the earliest (oldest) date from a list of dates---')

from datetime import datetime
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
earliest_date = min(dates_list)
print('earliest date = ', earliest_date)