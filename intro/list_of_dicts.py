number = int(input("number="))
print([{'single':el, 'square':el**2, 'cube':el**3} for el in list(range(1,number+1))])
