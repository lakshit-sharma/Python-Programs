# Write a Python program to display the current date and time.

import datetime
x=datetime.datetime.now()
print("Current Date & Time")
print(x.strftime("%d-%m-%Y %H:%M:%S %A"))