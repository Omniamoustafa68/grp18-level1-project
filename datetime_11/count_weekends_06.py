#program to count fri or sat in a specific month
from datetime import datetime
from dateutil.relativedelta import relativedelta
#inputs
m = 8
y= 2024
#program
custom_date = datetime(year=y, month=m, day=1)#1-7-2024

end_date = custom_date + relativedelta(months=1)#1-8-2024
weekend_counter=0
while custom_date < end_date:
    print(custom_date)
    # check for the custom date if it is fri | sat
    if custom_date.date().weekday() in [4, 5]: # fri = 4 , sat=5
        weekend_counter = weekend_counter +1
    custom_date = custom_date + relativedelta(days=1)# increasethe date by a day every iteration
print('count of weekend = ', weekend_counter)