# from datetime module import datetime class
from datetime import datetime
#from relativedelta module found in dateutil pkg  import relativedelta class
from dateutil.relativedelta import relativedelta

from datetime import datetime
from dateutil.relativedelta import relativedelta
print('---get the different between 2 dates---')
print('1- get the different between 2 dates in days as a total--')
today = datetime.now()
custom_date = datetime(year=2010, month=3, day=10)
different_in_days = today - custom_date
#print(different_in_days)
print(different_in_days.days)

print('2- get the different between 2dates in years ,months, days, using relativedelta module')
different_in_parts = relativedelta(today, custom_date)
print(different_in_parts)
print(different_in_parts.years, different_in_parts.months, different_in_parts.days)

