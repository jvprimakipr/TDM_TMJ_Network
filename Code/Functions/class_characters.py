class characters:
    def __init__(self):
        # auxiliares para contagem
        self.atendent_number = 0
        self.father_number = 0
        self.mother_number = 0
        self.figurante_number = 0
        self.child_number = 0

        # TDM
        self.mon = 'Mônica'
        self.ceb = 'Cebolinha'
        self.cas = 'Cascão'
        self.mag = 'Magali'
        self.moca = 'Monicão'
        self.floq = 'Floquinho'
        self.chov = 'Chovenista'
        self.min = 'Mingau'
        self.xav = 'Xaveco'
        self.franj = 'Franjinha'
        self.mmon = 'Mãe da Mônica'
        self.pmon = 'Pai da Mônica'
        self.mceb = 'Dona Cebola'
        self.pceb = 'Seu Cebola'
        self.mmag = 'Mãe da Magali'
        self.pmag = 'Pai da Magali'
        self.mcas = 'Mãe do Cascão'
        self.pcas = 'Pai do Cascão'
        self.san = 'Sansão'
        self.bid = 'Bidu'
        self.luc = 'Luca'
        self.den = 'Denise'
        self.pxav = 'Pai do Xaveco'
        self.mar = 'Marina'
        self.viv = 'Bruxa Viviane'
        self.bor = 'Bóris'
        self.dud = 'Dudu'
        self.mdud = 'Mãe do Dudu'

        # turma do Penadinho
        self.pen = 'Penadinho'
        self.fra = 'Frank'
        self.mum = 'Muminho'
        self.vam = 'Zé Vampir'
        self.lob = 'Lobi'
        self.alm = 'Alminha'
        self.cav = 'Zé Caveirinha'
        self.cra = 'Cranícola'

        # chico bento
        self.chi = 'Chico Bento'
        self.ros = 'Rosinha'
        self.pro = 'Dona Marocas'
        self.pad = 'Padre Lino'
        self.mchi = 'Dona Cotinha'
        self.nho = 'Nhô Lau'
        self.lel = 'Zé Lelé'
        self.mlel = 'Mãe do Zé Lelé'

        # tina
        self.rol = 'Rolo'
        self.tin = 'Tina'
        self.pip = 'Pipa'
        self.ser = 'Serginho'

        # piteco
        self.pit = 'Piteco'

        # astronauta
        self.ast = 'Astronauta'
    
    def atend(self, reset = False, n = 0):
        if n != 0:
            return f'Atendente {n}'
        elif reset:
            self.atendent_number = 0
        else:
            self.atendent_number += 1
            return f'Atendente {self.atendent_number}'
    
    def fat(self, reset = False, n = 0):
        if n != 0:
            return f'Pai {n}'
        elif reset:
            self.father_number = 0
        else:
            self.father_number += 1
            return f'Pai {self.father_number}'
    
    def mot(self, reset = False, n = 0):
        if n != 0:
            return f'Mãe {n}'
        elif reset:
            self.mother_number = 0
        else:
            self.mother_number += 1
            return f'Mãe {self.mother_number}'

    def fig(self, reset = False, n = 0):
        if n != 0:
            return f'Figurante {n}'
        elif reset:
            self.figurante_number = 1
        else:
            self.figurante_number += 1
            return f'Figurante {self.figurante_number}'
    
    def child(self, reset = False, n = 0):
        if n != 0:
            return f'Criança {n}'
        elif reset:
            self.child_number = 0
        else:
            self.child_number += 1
            return f'Criança {self.child_number}'

'''
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

    def san(self):
        return 'Sansão'
'''
