# Two more useful functions: strftime() and strptime() used for formatting and working with dates

from datetime import datetime

d1 = datetime.now()
print(d1)

# Print with /
strDate = d1.strftime("%d/%m/%Y, %H:%M:%S")
print(strDate)

ds = "12 April,2022"
dateObject = datetime.strptime(ds,"%d %B,%Y") # have to match the exact string with space and punctuations
print(dateObject)
