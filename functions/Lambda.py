# Lambda is an anonymous function

# Normal function is defined as below

def cubeTest(y):
    return y*y*y
print(cubeTest(5))

# The same fucntion can be return as below

ret = lambda y:y*y*y
print(ret(5))

# String operation using lambda

strList1 = ["This","is","a","Python","Terminal"]
print(len(strList1))

# Used Map cause - in lambda list expected at most 1 argument & 'function' object must be iterable
strList2 = list(map(lambda s:s.upper()+"!",strList1))
print(strList2)

# below doesn't work cause map is not used.
##strList2 = list(lambda s:s.upper()+"!",strList1)
##print(strList3())
## or
##strList2 = list(lambda s:s.upper()+"!")
##print(strList2(strList1))
##strList2 = list(lambda s:s.upper()+"!")
##print(strList2(strList1[3]))

# we ca use condition in lambda
retval = lambda x:x*2 if x<5 else x
print(retval(3))
print(retval(6))

# filter operation in lambda

strList3 = list(filter(lambda s:len(s)>3,strList1))
print(strList3)

numList=[1,2,3,4,5,6,7,8,9,0]
oddN=list(filter(lambda n:n%2==1,numList))
print(oddN)
