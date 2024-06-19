# sorted() to sort any iterable object.

lst = [50, 60, 40, 10, 20, 100, 45, 95, 120, 115, 75]

sortedList = sorted(lst)
print(sortedList)

sortedList = sorted(lst, reverse=True)
print(sortedList)

lstData = [("AAA", 101), ("DDD", 10), ("EEE", 115), ("CCC", 100), ("DDD", 110)]
lstsorted = sorted(lstData)
print(lstsorted)

# now to sort based on the number use lambda function to use the number as key for sorting

SortedData = sorted(lstData, key=lambda x: x[1])
print(SortedData)

# sorted() for sub-string

EmpIds = ['CS001','IT050','EC040','EE100','IT001']
print(sorted(EmpIds))
sortedIds=sorted(EmpIds,key = lambda x:int(x[2:]))
print(sortedIds)


