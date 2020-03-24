'''
Write a base class animal with twoderived classes bird and dog that change the class variable 'movement'.
__str__ method should reflect the different class objects.
The comparisson operator should compare objects based on the age however it should be able to compare an object with an integer(objets's age with the integer)
'''
class animal():
    
    movement = None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'We have {} named {} which is {} years old.'.format(self.__class__.__name__, self.name, self.age)
    
    def get_old(self, additional_ages=1):
        self.age += additional_ages

    def __eq__(self, other):
        if isinstance(other, animal): # other is animal object
            return self.age == other.age
        elif isinstance(other, int): #other is integer
            return self.age == other
        else:
            raise TypeError("Only integers or animals are allowed")

   
class bird(animal):

    movement = 'flying'
    
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def __str__(self):
        return super().__str__() + " It is moving by {}.".format(__class__.movement)

    
class dog(animal):
    
    movement = 'running'
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def __str__(self):
        return super().__str__() + " It is moving by {}.".format(__class__.movement)

if __name__ == '__main__':
    a = animal('Charlie', 2)
    print(a)
    b = dog('John', 3)
    print(b)
    p = bird('Tweety', 1)
    print(p)
    p.get_old()
    print(p)
