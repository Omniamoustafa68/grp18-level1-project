print('--Check if all dates in a list are in the same month--')
from datetime import datetime

dates_list = [
    datetime(2023, 7, 31),
    datetime(2023, 7, 15),
    datetime(2023, 7, 15),
    datetime(2023, 8, 1)
]

same_month = dates_list[0].month
# print(same_month)
same_flag = True
for date in dates_list:
    if same_month != date.month:
        same_flag = False
        break

if same_flag == True:
    print('All Months are with the same months = ', same_month)
else:
    print('all date are not the same month ')

