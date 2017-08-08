# A set is like a list but cannot contain duplicate characters
a_set = {1, 2, 3, 4, 5}
b_set = {3, 5, 6, 7, 8}

#Checking if an item is present in the list
2 in a_set # True
7 in a_set # False

# A set is not indexed
#Set operations
print("The union of the sets: ", a_set | b_set)
print("The intersection of the sets: ", a_set & b_set)
print("The difference of the sets a-b: ", a_set - b_set)
print("The difference of the sets b-a: ", b_set - a_set)
print("The symmetric difference of the sets: ", a_set ^ b_set)

#Adding to a set
a_set.add(10)
print ("A new item has been added to the list", a_set)

#Removing the first item from the set
a_set.pop()
print ("The element has been removed from the set", a_set)

#Removing a specific item
a_set.remove(5)
print (a_set)

#Iterating through a set
for i in a_set.difference(b_set):
    print (i)