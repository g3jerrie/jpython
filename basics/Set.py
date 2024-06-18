#Set: Set is a unordered unique collecton of elements.
#Set is represented by {} and also set()

aSet = {}
print("initialy aSet is of the type - ", type(aSet))
aSet = {100,200,30,40,50,100,200,90}
print("after assigning values aSet is of the type - ", type(aSet))
bSet = set()
print("initialy bSet is of the type - ", type(bSet))
bSet = {300,100,200,60,75,110,45,55}
print(aSet)
print(aSet.union(bSet))
print(aSet.intersection(bSet))
print(aSet-bSet) #shows the aSet elements which are not availble in bSet
print(bSet-aSet) #shows the bSet elements which are not availble in aSet

