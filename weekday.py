#program that outputs whether or not today is a weekday

#Author: Francesco Troja

from datetime import datetime
today = datetime.today().isoweekday()

if today < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

