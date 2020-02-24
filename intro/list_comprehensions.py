# List comprehension
list_1 = [1, -2, 3, 5, -2, -1, 7, 12, 8]

# List with all values of list1 squared
list_2 = [value**2 for value in list_1]
print("The vales {} squared are {}".format(list_1, list_2))

# List with all values of list1 that are positive
list_3 = [value for value in list_1 if value >= 0]
print("The positive vales of {} are {}".format(list_1, list_3))
