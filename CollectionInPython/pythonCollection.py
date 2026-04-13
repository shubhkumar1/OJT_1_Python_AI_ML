'''
Collection in Python
    1. List
    2. Set
    3. Tuple
    4. Dictionary
'''


print("\nCollection in Python\n-------------------")

#--------List--------(Ordered, Changeable, allow Duplicate)
print("\nList\n-------------------")
listVar = [1,2,3,4,5,2]
print(listVar)
print(listVar[3])
print(type(listVar))

#------Set-----------(Unordered, unchangeable, don't allow duplicate)
print("\nSet\n-------------------")
setVar = {1,2,3,4,"Sahil",3,5}
print(setVar)
print(type(setVar))

#-------Tuple--------(orderd, Unchangeable, allow Duplicate)
print("\nTupple\n-------------------")
tupleVar = (1,3,5,3,)
print(tupleVar)
print(tupleVar[2])
print(type(tupleVar))

#------Dictionary------(Orderd, Changeable, don't allow Duplicate)
print("\nDictionary\n-------------------")
dictVar = {
    "name" : "Shubham",
    "dept" : "BCA",
    "roll" : "23MCRBS580111334"
}
print(dictVar)
print(type(dictVar))