import calendar

#Weekheader function 
print(calendar.weekheader(3))
print()
#Firstweekday function 
print(calendar.firstweekday())
print()
#Month function 
print(calendar.month(2024,4,10))
#Monthcalendar 
print(calendar.monthcalendar(2024,4))
#Calendar function 
print(calendar.calendar(2024,2))
#Weekday function 
today = calendar.weekday(2069,10,31)
print(today)
#Isleap function 
isleap_day=calendar.isleap(2024)
print()
print(isleap_day)
print()
#Leapdays function 
how_many_leaps_day = calendar.leapdays(2024,2040)
print(how_many_leaps_day)