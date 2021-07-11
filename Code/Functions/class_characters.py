class characters:
    def __init__(self):
        self.atendent_number = 0
        self.father_number = 0
        self.mother_number = 0
        self.figurante_number = 0
        self.child_number = 0
    
    def atend(self, reset = False):
        if reset:
            self.atendent_number = 1
        else:
            self.atendent_number += 1
        return f'Atendente {self.atendent_number}'
    
    def fat(self, reset = False):
        if reset:
            self.father_number = 1
        else:
            self.father_number += 1
        return f'Atendente {self.father_number}'
    
    def mot(self, reset = False):
        if reset:
            self.mother_number = 1
        else:
            self.mother_number += 1
        return f'Atendente {self.mother_number}'

    def fig(self, reset = False):
        if reset:
            self.figurante_number = 1
        else:
            self.figurante_number += 1
        return f'Atendente {self.figurante_number}'
    
    def child(self, reset = False):
        if reset:
            self.child_number = 1
        else:
            self.child_number += 1
        return f'Atendente {self.child_number}'

    def mon(self):
        return 'Mônica'

    def ceb(self):
        return 'Cebolinha'

    def cas(self):
        return 'Cascão'

    def mag(self):
        return 'Magali'

    def moca(self):
        return 'Monicão'

    def floq(self):
        return 'Floquinho'

    def chov(self):
        return 'Chovenista'

    def xav(self):
        return 'Xaveco'

    def franj(self):
        return 'Franjinha'

    def mmon(self):
        return 'Mãe da Mônica'

    def pmon(self):
        return 'Pai da Mônica'

    def mceb(self):
        return 'Dona Cebola'

    def pceb(self):
        return 'Seu Cebola'

    def mmag(self):
        return 'Mãe da Magali'

    def pmag(self):
        return 'Pai da Magali'

    def mcas(self):
        return 'Mãe do Cascão'

    def pcas(self):
        return 'Pai do Cascão'
