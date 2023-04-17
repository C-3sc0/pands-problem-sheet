#program that outputs whether or not today is a weekday

#Author: Francesco Troja

from datetime import datetime
today = datetime.today().isoweekday()

if today < 5: #since isoweekday method returns the day of the week as int, where Monday is 1 and Sunday 7, if the current day is between Monday and Thursday the first statement will be printed  
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
