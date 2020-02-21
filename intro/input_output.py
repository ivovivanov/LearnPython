#line ending of print() function
print('one', 'two', 'three', sep='|', end='')
print() #This will just print '\n'
#line ending of print() function
print("Enter var:", end='')
var = input()
print("Type of variable is of type: {}".format(type(var)))

#We can do prompt text within input() function
var = input("Enter var:")
print("var is equal to {}".format(var))
