from datetime import datetime,date
my_date = date.today()                      # Show actual date
year, week_num, day_of_week = my_date.isocalendar()

print(week_num)

