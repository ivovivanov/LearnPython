# Sum of digits of a number
# Enter number from keyboard and convert to <class 'int'>
number = int(input("number="))
print("The sum of digits of {}".format(number), end='')
# Calculate the sum
sum_of_digits = 0
while number:
  sum_of_digits += number%10
  number //= 10
print(" is {}.".format(sum_of_digits))
