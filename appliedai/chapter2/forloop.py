

for i in range(100):
    print("i is "+str(i))

    print("Formattted i is {0}".format(i))

    print ("Hello {name},{greeting}".format(name="Vineet",greeting="Welcome to the Python world!!!"))

print("============================================================================")

print("The story of {0},{1} and other {other}".format("Vineet","Badoni", other=""))

print ("Example 2")

for i in range(1,10,2):
    print ("i is {0}.".format(i))
    
idx1,idx2 = 10,20

print("Another range example")

for i in range(idx1,idx2):
    print("i is {0}.".format(i))