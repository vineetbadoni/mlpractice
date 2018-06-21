'''
List:
(1) Mutable
(2) Can have different data
'''

l1 = [3,2.0,'1',[2,1],['2','1']]

print ("List1 is {}".format(l1))

l2 = [3,2,1]

print ("List2 is {}".format(l2))

l1.append(l2)

print("l1.append(l2)")

print ("List1 is {}".format(l1))

l1.extend(l2)

print("l1.extend(l2)")

print ("List1 is {}".format(l1))

'''
List operations
(1) delete
(2) pop
(3) sorted - mutable vs immutable i.e sorted() vs .sort
'''
print("l2 is {0} and sorted version is {1}.".format(l2,sorted(l2)))

#Error as list contains string and integers and float. It should contain compatible values.
#print("l1 is {0} and sorted version is {1}.".format(l1,sorted(l1)))

# Delete operations
l1.remove("1")
print("l1 after deletion {0}".format(l1))

#Delete at index i
del l1[1]
print("l1 after deletion {0} using index".format(l1))

#Pop an element
popedVal = l1.pop(1)
print("l1 after Pop {0} using index".format(l1))

#Reverse sorted

print("l1 reverse sorted {0}".format(sorted(l2,reverse=True)))

#Search
print("Find {0} in {1} is {2}.".format(1,l1,1 in l1))

print("Find {0} not in {1} is {2}.".format("six",l1,"six" not in l1))