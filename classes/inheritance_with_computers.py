'''Class structure:

+computer
|-desktop_pc
|-server
|-workstation
`-laprop


'''
class computer():
    ram_mult = 1
    proc_mult = 1

    def __init__(self, ram, proc_freq):
        self.ram = ram
        self.proc_freq = proc_freq
    
    def __str__(self):
        return 'This is a {} with the following specs:\n cpu: {} Ghz\n ram: {} Gb\n'.format(self.__class__.__name__, self.proc_freq, self.ram)

    def score(self):
        return self.ram_mult*self.ram + self.proc_mult*self.proc_freq*(self.proc_number if 'proc_number' in self.__dict__ else 1)

    def __eq__(self, other):
        return self.score() == other.score()

    def __ge__(self, other):
        return self.score() >= other.score()
    
    def __gt__(self, other):
        return self.score() > other.score()

    def __le__(self, other):
        return self.score() <= other.score()
    
    def __lt__(self, other):
        return self.score() < other.score()


class desktop_pc(computer):
    ram_mult = 1
    proc_mult = 2

    def __init__(self, ram, proc_freq, case_type):
        super().__init__(ram, proc_freq)
        self.case_type = case_type


class laptop(computer):
    pass

class server(computer):
    ram_mult = 2
    proc_mult = 2

    def __init__(self, ram, proc_freq, proc_number):
        super().__init__(ram, proc_freq)
        self.proc_number = proc_number

class workstation(computer):
    ram_mult = 1.5
    proc_mult = 1.5

    def __init__(self, ram, proc_freq, proc_number):
        super().__init__(ram, proc_freq)
        self.proc_number = proc_number
    
    def __str__(self):
        return 'This is a {} with the following specs:\n cpu: {} x {} Ghz\n ram: {} Gb\n'.format(self.__class__.__name__, self.proc_number, self.proc_freq, self.ram)

  
if __name__ == '__main__':
    a = computer(4,3)
    a1 = computer(4,4)
    print('a score is {}'.format(a.score()))
    print('a1 score is {}'.format(a1.score()))
    print(a==a1)
    b = desktop_pc(4,4, 'tower')
    print(a)
    print(b)
    c = server(4, 4, 2)
    print(c)

'''
computer_ratio = 1/1 ram/proc 1*4 + 1*3 = 7
                             1*6 + 1*3 = 9
desktop_pc = 1/2 ram/prc 1*4+2*5
server = 2/2 ram/proc
'''
