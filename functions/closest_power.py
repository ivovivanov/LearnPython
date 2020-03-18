def closest_power(a: int, b: int) -> int:
    result, counter = a, 1
    while result < b:
        counter+=1
        result = a**counter
    return result if result-b<b - a**(counter-1) else a**(counter-1)

if __name__ == '__main__':
    print(closest_power(3,50))
