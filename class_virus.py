class virus():
    area = 'medicine'
    def __init__(self, name, risk_level):
        self.name = name
        self.set_risklevel(risk_level)
    
    def __str__(self):
        return 'This is a virus named {} with a risk level of {}!'.format(self.name, self.risk_level)

    def __eq__(self, other):
        return self.risk_level == other.risk_level
    
    def __gt__(self, other):
        return self.risk_level > other.risk_level
    
    def __ge__(self, other):
        pass
    
    def set_risklevel(self, risk_level):
        self.risk_level = risk_level if risk_level in range(1,6) else 1
    
if __name__ == '__main__':
    a = virus('corona', -3)
    print(a)
    b = virus('ebola', 5)
    print(b)
    print(a == b)
