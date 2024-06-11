#here we willshow all basic operations on datetime

#from datetime module import datetime class
from datetime import datetime
print('---1- get the current date and time--')
today = datetime.now()
print(today)

print('---2- get only date or time or their parts ---')
print(today.date())
print(today.date().day)
print(today.date().month)
print(today.date().year)
print(today.date().weekday())   #which day in a week? start by monday = 0

print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)

print('---3- reformatting date, time--- | we use strftime()function-----')
print('convert date into string using strftime() function---')
print(today)
print(today.strftime('%d-%m-%Y'))#day, month, Year
print(today.strftime('%d-%m-%Y-%y-%W'))# day, month, year, yr, week per year
print(today.strftime('%B-%b-%A-%a'))# Month - mon - Day - dy
#timing format
print(today.strftime('%H-%M-%S'))#HOUR24 - MINUTES - SECOUNDS
print(today.strftime('%I-%M-%S-%p'))#hours 12 - minutes - secounds - am pm


print('4- creat a custom date 21-septemper-2023---')
print('----1st way : datetime object using constructor----')

custom_date = datetime(year=2023, month=9, day=21)
print(custom_date)

print('---2nd way: by converting a string into date using strptime() function')
date_string_style = '21-9-2023'#string
new_custom_date = datetime.strptime(date_string_style, '%d-%m-%Y')
print(new_custom_date)#datetime

print('------5- comparison----')

if today.date()> custom_date.date():
    print('today is newer than custom date')
elif today.date()<custom_date.date():
    print('today is older than custom date')
else:
    print('2 dates are equal')

