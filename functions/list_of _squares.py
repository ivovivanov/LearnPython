'''
Function accepts random number of integers as functions arguments.
Function should return a list of squars of the positive integers.
'''

def list_of_squares(*args):
    result = list()
    for arg in args:
        if arg > 0:
            result.append(arg**2)
    return result

def list_of_squares_v2(*args):
    return [arg**2 for arg in args if arg > 0]

if __name__ == '__main__':
    print(list_of_squares(1,3,-1,-4,-2,7,1,-8,0,9))
    print(list_of_squares_v2(1,3,-1,-4,-2,7,1,-8,0,9))
