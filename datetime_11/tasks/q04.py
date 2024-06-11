print('--Count occurrences of a specific date in a list--')
from datetime import datetime
dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1),
]
given_date = datetime(2023, 8, 15)

count_occurrences = 0
for date in dates_list:
    if date == given_date:
        count_occurrences = count_occurrences + 1

print(given_date, 'occurs', count_occurrences, 'Times')
