class characters:
    def __init__(self):
        # auxiliar para diferenciar os gibis
        self.comic_book = ''

        # auxiliares na marcação das histórias
        self.beg = 'begin'
        self.end = 'end'
        
        # auxiliares para contagem
        self.figurant_number = 0
        self.shade_number = 0
        self.attendant_number = 0
        self.father_number = 0
        self.mother_number = 0        
        self.child_number = 0
        
        # God
        self.mau = 'Maurício de Souza'
        
        ###############################
        ####### TURMA PRINCIPAL #######
        ###############################
        
        # Protagonistas
        self.mon = 'Mônica'
        self.ceb = 'Cebolinha'
        self.mag = 'Magali'
        self.cas = 'Cascão'
        
        # Pets
        self.san = 'Sansão'
        self.moca = 'Monicão'
        self.floq = 'Floquinho'
        self.min = 'Mingau'
        self.chov = 'Chovinista'
        self.bid = 'Bidu'
        self.xim = 'Ximbuca'
        self.bor = 'Bóris'
        self.manf = 'Manfredo'
        self.ave = 'Aveia'
        self.duq = 'Duque'
        self.zesq = 'Zé Esquecido'
        self.bug = 'Bugu'
        self.rad = 'Radar' # cão-guia da Dorinha
        
        # Secundários (Masculino)
        self.franj = 'Franjinha'
        self.xav = 'Xaveco'
        self.doc = 'Do Contra'
        self.nim = 'Nimbus'
        self.dud = 'Dudu'
        self.luc = 'Luca'
        self.hum = 'Humberto'
        self.tit = 'Titi'
        self.jer = 'Jeremias'
        self.man = 'Manezinho'
        self.anj = 'Anjinho'
        self.quin = 'Quinzinho'
        self.zlui = 'Zé Luís'
        self.blo = 'Bloguinho'
        self.tv = 'Teveluisão'
        self.fabbp = 'Fabinho Boa Pinta'
        self.ric = 'Ricardinho'
        self.ber = 'Bernardinho'
        self.nicdem = 'Nico Demo'
        
        # Secundárias (Feminino)
        self.den = 'Denise'
        self.mar = 'Marina'
        self.marceb = 'Maria Cebolinha'
        self.carfru = 'Carminha Frufru'
        self.marcas = 'Maria Cascuda'
        self.xab = 'Xabéu'
        self.ani = 'Aninha'
        self.dor = 'Dorinha'
        
        # Pais e Mães
        self.mmon = 'Dona Luísa'
        self.pmon = 'Seu Souza'
        self.mceb = 'Dona Cebola'
        self.pceb = 'Seu Cebola'
        self.mmag = 'Dona Lili'
        self.pmag = 'Seu Carlito'
        self.mcas = 'Dona Lurdinha'
        self.pcas = 'Seu Antenor'
        self.mxav = 'Dona Xarlene'
        self.pxav = 'Seu Xavier'
        self.mdud = 'Dona Cecília'
        self.pdud = 'Seu Durval'
        self.mtv = 'Mãe do Teveluisão'
        self.mdor = 'Mãe da Dorinha'
        self.mdoc = 'Mãe do Do Contra / Nimbus'
        
        # Tios(as), Avôs(ós)
        self.tnen = 'Tia Nena'
        self.tpep = 'Tio Pepo'
        self.vxep = 'Vó Xepa'
        
        # Vilões
        self.cap = 'Capitão Feio'
        self.viv = 'Bruxa Viviane'
        self.spa = 'Professor Spada / Doutor Spam'
        self.cab = 'Cabeleira Negra'
        self.lor = 'Lorde Coelhão'
        self.yuk = 'Yuka'
        self.ark = 'Arkanum'
        self.kra = 'Kraker'
        
        # Adultos (em geral)
        self.lou = 'Louco'
        self.juc = 'Seu Juca'
        self.fal = 'Prof Falconi'
        self.van = 'Vanda'
        self.val = 'Valéria'
        
        #Seres Míticos
        self.ebor = 'Bóreas'
        self.ezep = 'Zephyrus'
        self.eeur = 'Euros'
        self.enot = 'Notus'
        self.spau = 'São Paulo'
        
        #Seres Tecnológicos
        self.rob = 'Robóris'
        
        # Vida Real
        self.ali = 'Alice'
        
        ###############################
        ##### TURMA DO PENADINHO ######
        ###############################
        
        self.pen = 'Penadinho'
        self.alm = 'Alminha'
        self.mum = 'Muminho'
        self.zvam = 'Zé Vampir'
        self.fra = 'Frank'
        self.lob = 'Lobi'
        self.cra = 'Cranicóla'
        self.zcav = 'Zé Caveirinha'
        self.mor = 'Dona Morte'
        self.ceg = 'Dona Cegonha'

        ###############################
        #### TURMA DO CHICO BENTO #####
        ###############################
        
        # Crianças
        self.chi = 'Chico Bento'
        self.ros = 'Rosinha'
        self.zlel = 'Zé Lelé'
        self.marcaf = 'Maria Cafufa'
        self.zroc = 'Zé da Roça'
        self.hir = 'Hiro'
        self.pzec = 'Primo Zeca'
        self.gen = 'Genesinho'
        self.marcaf = 'Maria Cafufa'
        
        # Adultos
        self.mchi = 'Dona Cotinha'
        self.pchi = 'Nhô Bento'
        self.mlel = 'Dona Lalá'
        self.plel = 'Seu Leocádio'
        self.prof = 'Dona Marocas'
        self.pad = 'Padre Lino'
        self.nho = 'Nhô Lau'
        self.vdit = 'Vó Dita'
        
        # Animais
        self.fid = 'Fido'
        self.tor = 'Torresmo'
        self.gis = 'Giselda'
        self.mim = 'Mimosa'

        ###############################
        ######## TURMA DA TINA ########
        ###############################
        
        self.tin = 'Tina'
        self.rol = 'Rolo'
        self.pip = 'Pipa'
        self.zec = 'Zecão'
        self.pat = 'Patricinha'
        self.ser = 'Serginho'
        self.ton = 'Toneco'
        self.vov = 'Vovoca'

        ###############################
        ## TURMA DO PITECO E HORÁCIO ##
        ###############################
        
        # Humanos
        self.pit = 'Piteco'
        self.thu = 'Thuga'
        self.bol = 'Bolota'
        self.ogr = 'Ogra'
        self.bel = 'Beleléu'
        self.var = 'Vartolo'

        # Dinossauros
        self.hor = 'Horácio'
        self.luci = 'Lucinda'
        self.tec = 'Tecodonte'
        self.sim = 'Simone'
        
        ###############################
        ##### TURMA DO ASTRONAUTA #####
        ###############################
        
        self.ast = 'Astronauta'
        self.rit = 'Ritinha'
        self.comp = 'Computador'
        self.mast = 'Natalina'
        self.past = 'Astrogildo'

        ###############################
        ##### TURMA DO PAPA CAPIM #####
        ###############################
        
        self.pap = 'Papa-Capim'
        self.caf = 'Cafuné'
        self.jur = 'Jurema'
        self.cai = 'Caiapopó'
        self.paj = 'Pajé'
        self.cac = 'Cacique'

        ###############################
        ######## TURMA DA MATA ########
        ###############################
        
        self.jot = 'Jotalhão'
        self.rap = 'Raposão'
        self.coe = 'Coelho Caolho'
        self.tar = 'Tarugo'
        self.naj = 'Rita Najura'
        self.rei = 'Rei Leonino'
        self.cax = 'Luís Caxeiro'
    
    def fig(self, n = 0, add = '', reset = False):
        if n != 0:
            return f'Figurante {n} - {self.comic_book}'
        elif add != '':
            return f'Figurante {self.figurant_number + add} - {self.comic_book}'
        elif reset:
            self.figurant_number = 0
        else:
            self.figurant_number += 1
            return f'Figurante {self.figurant_number} - {self.comic_book}'
    
    def figs(self, n):
        figs = []
        for i in range(n):
            figs.append(self.fig())
        return figs
    
    def shade(self, n = 0, add = '', reset = False):
        if n != 0:
            return f'Sombra {n} - {self.comic_book}'
        elif add != '':
            return f'Sombra {self.shade_number + add} - {self.comic_book}'
        elif reset:
            self.shade_number = 0
        else:
            self.shade_number += 1
            return f'Sombra {self.shade_number} - {self.comic_book}'
    
    def shades(self, n):
        shades = []
        for i in range(n):
            shades.append(self.shade())
        return shades
    
    def att(self, n = 0, add = '', reset = False):
        if n != 0:
            return f'Atendente {n} - {self.comic_book}'
        elif add != '':
            return f'Atendente {self.attendant_number + add} - {self.comic_book}'
        elif reset:
            self.attendant_number = 0
        else:
            self.attendant_number += 1
            return f'Atendente {self.attendant_number} - {self.comic_book}'

    def fat(self, n = 0, add = '', reset = False):
        if n != 0:
            return f'Pai {n} - {self.comic_book}'
        elif add != '':
            return f'Pai {self.father_number + add} - {self.comic_book}'
        elif reset:
            self.father_number = 0
        else:
            self.father_number += 1
            return f'Pai {self.father_number} - {self.comic_book}'
    
    def mot(self, n = 0, add = '', reset = False):
        if n != 0:
            return f'Mãe {n} - {self.comic_book}'
        elif add != '':
            return f'Mãe {self.mother_number + add} - {self.comic_book}'
        elif reset:
            self.mother_number = 0
        else:
            self.mother_number += 1
            return f'Mãe {self.mother_number} - {self.comic_book}'
    
    def child(self, n = 0, add = '', reset = False):
        if n != 0:
            return f'Criança {n} - {self.comic_book}'
        elif add != '':
            return f'Criança {self.child_number + add} - {self.comic_book}'
        elif reset:
            self.child_number = 0
        else:
            self.child_number += 1
            return f'Criança {self.child_number} - {self.comic_book}'
    
    def kids(self, n):
        kids = []
        for i in range(n):
            kids.append(self.child())
        return kids

    def reset(self):
        self.fig(reset = True)
        self.shade(reset = True)
        self.att(reset = True)
        self.mot(reset = True)
        self.fat(reset = True)
        self.child(reset = True)
