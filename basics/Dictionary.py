# Dictionary: Is represented with a Key:Value pair, where Key has to be unique.
# Dictionary is also reprsented as {}

a = {}
print("a is of the type: ",type(a))
a = {"One":1,"Two":2,"Three":3}
print(a)
print(a["Two"])
print(a.get("Two"))
print(a.keys())
print(a.values())
for i in a:
    print(i,":",a[i])

