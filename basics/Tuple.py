# Tuple: Represents an immutable row/record
# Tuple is represented as ()
# we can't add any record to the already intialised Tupple


rec = ()
print("rec is of type",type(rec))
#empDB as List of Tupple
empDB = [(101,"AAA",100000),(102,"BBB",200000),(103,"CCC",300000)]
print("empDB is of type",type(empDB))
print("empDB element is of type",type(empDB[1]))
print("empDB element's content is of type",type(empDB[1][0]),"&",type(empDB[1][1]))
print(empDB)
print(empDB[1])
print(empDB[1][2])
