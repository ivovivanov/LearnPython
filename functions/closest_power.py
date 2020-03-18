'''
Write a function that returns the closest power of 'a' to 'b', where 'a' and 'b' are given integer number arguments
'''
def closest_power(a: int, b: int) -> int:
    result, counter = a, 1
    while result < b:
        counter+=1
        result = a**counter
    return result if result-b<b - a**(counter-1) else a**(counter-1)

if __name__ == '__main__':
    print(closest_power(3,50))
