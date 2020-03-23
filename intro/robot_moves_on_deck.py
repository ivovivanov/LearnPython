'''
A robot can move on a deck in up, down, right or left with a given number of step. First read a starting position ( e.g. 2,3 ). Then read  moves (e.g. Down 4 or Left 6 or Up 1 or Right 7 etc.). Calculate the position of the robot after all the moves are done from the starting position.
'''
if __name__ == '__main__':
    position = input('Enter the starting postion (e.g. 1,2): ')
    position = [int(number) for number in position.split(',')]
    print('Enter moves - one per line (e.g. DOWN 1):')
    while True:
        move = input()
        if not move:
            break
        move = move.split(' ')
        direction = move[0].upper()
        number_of_steps = int(move[1])
        
        if direction == 'UP':
            position[0] += number_of_steps
        elif direction == 'DOWN':
            position[0] -= number_of_steps
        elif direction == 'RIGHT':
            position[1] += number_of_steps
        elif direction == 'LEFT':
            position[1] -= number_of_steps
        else:
            pass

    print('Final position of robot is {},{} !!!'.format(position[0], position[1]))
