#List

lst1 = [10,20,"This is String",[40,50],100]
print(len(lst1))
print("The first element is: ",lst1[0])
print("The first element is: ",lst1[2])
print("The first element is: ",lst1[3])
print("The first element is: ",lst1[3][1])
lst1.append(200)
print(lst1)
for x in lst1:
    print(x)
lst1.append(20) # List allow duplicate, where as Set doesn't allow duplicate
print(lst1)


lst2=[10,20,30,40,50,70,90]

# to create another list with the values from lst2 with values greater than 30

lst3=[]
for x in lst2:
    if(x>30):
        lst3.append(x)
print("The new list is: ", lst3)

# Using List comprehension - compact syntax

lst4 = [x for x in lst2 if(x>30)]
print(lst4)

lst4.append(100)
print(lst4)
lst4.insert(2,60)
print(lst4)
lst4.reverse()
print(lst4)
print(len(lst4))
