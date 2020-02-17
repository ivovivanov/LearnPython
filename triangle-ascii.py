ran = input()
print("type of ran is" , type(ran))
for x in range(0,int(ran)):
    for y in range(x,int(ran)):
        print('*', end="")
    print()
print()
