# datetime package
# working with datetime object

import datetime


dt = datetime.datetime.now()
print(dt)

d1= datetime.date(2024,6,26)
print(d1)

d2 = datetime.date(2024,6,5)
print(d2)

print(d2 -d1)

d3 = datetime.date.today()
print(d3)
print("Current Year:",d3.year)
print("Current Month:",d3.month)
print("Current Day:",d3.day)