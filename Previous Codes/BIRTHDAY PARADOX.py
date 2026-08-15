import random
import datetime
birthday = []
for i in range (1,51) :
    year = random.randint(1921,2023)
    if(year%4==0 and year%100!=0 or year%400==0) :
        leap = 1
    else :
        leap = 0
    month = random.randint(1,12)
    if(month==2 and leap==1) :
        day = random.randint(1,29)
    elif(month==2 and leap==0) :
        day = random.randint(1,28)
    elif(month%2==0 and month>7) :
        day = random.randint(1,31)
    elif(month%2!=0 and month<=7) :
        day = random.randint(1,31)
    else :
        day = random.randint(1,30)
    dd = datetime.date(year,month,day)
    day_of_year = dd.timetuple().tm_yday
    birthday.append(day_of_year)
    birthday.sort()
for i in birthday :
    print(i)