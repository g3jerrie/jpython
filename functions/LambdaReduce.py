# Lambda function using Reduce
# To find out the highest number using lambda functions and reduce

from functools import reduce

lst = [50,60,40,10,20,100,45,95,120,115,75]

highestNumber = reduce(lambda a,b : a if a>b else b, lst)
print("The greatest value is:",highestNumber)