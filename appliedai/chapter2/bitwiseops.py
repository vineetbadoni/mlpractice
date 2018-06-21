"""
Bitwise operators in Python
Operator	Meaning	Example
&	Bitwise AND	x& y = 0 (0000 0000)
|	Bitwise OR	x | y = 14 (0000 1110)
~	Bitwise NOT	~x = -11 (1111 0101)
^	Bitwise XOR	x ^ y = 14 (0000 1110)
>>	Bitwise right shift	x>> 2 = 2 (0000 0010)
<<	Bitwise left shift	x<< 2 = 40 (0010 1000)
"""

a,b=10,4

print ("a & b is {0}.".format(a&b))

print ("a & b is {0}.".format(a|b))

print ("a & b is {0}.".format(~b))

#List
l=[1,2,3]

print (1 in l)

print (4 in l)

print (3 not in l)

#Dictionary
dict = ["1:2"]

print("2" in dict)