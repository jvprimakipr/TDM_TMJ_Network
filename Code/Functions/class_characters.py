class characters:
    def __init__(self, cb = ''):
        # Auxiliar para diferenciar os gibis
        self.comic_book = cb

        # Auxiliares na marcação das histórias
        self.beg = 'begin'
        self.end = 'end'
        self.cb = self.comic_book + ' '
        
        # Auxiliares para contagem
        self.figurant_number = 0
        self.shade_number = 0
        self.attendant_number = 0
        self.father_number = 0
        self.mother_number = 0        
        self.child_number = 0
        self.student_number = 0
        self.animal_number = 0
        self.monster_number = 0
        self.dino_number = 0
        self.caveman_number = 0
        self.crowd_number = 0
        self.list_crowds = []
        
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
        
        # Secundárias (Feminino)
        self.den = 'Denise'
        self.mar = 'Marina'
        self.marceb = 'Maria Cebolinha'
        self.carfru = 'Carminha Frufru'
        self.marcas = 'Maria Cascuda'
        self.xab = 'Xabéu'
        self.ani = 'Aninha'
        self.dor = 'Dorinha'
        self.ver = 'Verinha'
        
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
        self.toni = 'Tonhão da Rua de Baixo'
        
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
        self.mdoc = 'Dona Keiko'
        self.pdoc = 'Seu Nimbão'
        self.mtv = 'Mãe do Teveluisão'
        self.mdor = 'Mãe da Dorinha'
        
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
        
        # Adultos (em geral)
        self.lou = 'Louco'
        self.juc = 'Seu Juca'
        
        #Seres Míticos
        self.spau = 'São Paulo' 
        
        # Vida Real
        self.ali = 'Alice'
        
        ###############################
        #### TURMA DA MÔNICA JOVEM ####
        ###############################
        
        #Jovens
        self.ire = 'Irene'
        
        #Adultos
        self.fal = 'Prof Falconi'
        self.rub = 'Prof Rubens'
        self.jor = 'Prof Jorge'
        self.van = 'Vanda'
        self.val = 'Valéria'
        
        #Outros
        self.ebor = 'Bóreas'
        self.ezep = 'Zephyrus'
        self.eeur = 'Euros'
        self.enot = 'Notus'
        self.yuk = 'Yuka'
        self.ark = 'Arkanum'
        self.kra = 'Kraker'
        self.robs = 'Robóris'
        self.usa = 'Princesa Usagi Mimi'
        self.rob = 'Robô'
        self.imp = 'Imperador Usagi'
        self.kam = 'Lorde Kamen'
        
        ###############################
        ####### TURMA DOS PETS ########
        ###############################
        
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
        self.rad = 'Radar'
        
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
    
    # Adiciona um id em cada personagem genérico
    def ID(self, name):
        return self.comic_book + ' ' + name
    
    def fig(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Figurante {n}')
        elif add != '':
            return self.ID(f'Figurante {self.figurant_number + add}')
        elif reset:
            self.figurant_number = 0
        else:
            self.figurant_number += 1
            return self.ID(f'Figurante {self.figurant_number}')
    
    def figs(self, n):
        return [self.fig() for i in range(n)]
    
    def shade(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Sombra {n}')
        elif add != '':
            return self.ID(f'Sombra {self.shade_number + add}')
        elif reset:
            self.shade_number = 0
        else:
            self.shade_number += 1
            return self.ID(f'Sombra {self.shade_number}')
    
    def shades(self, n):
        return [self.shade() for i in range(n)]
    
    def att(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Atendente {n}')
        elif add != '':
            return self.ID(f'Atendente {self.attendant_number + add}')
        elif reset:
            self.attendant_number = 0
        else:
            self.attendant_number += 1
            return self.ID(f'Atendente {self.attendant_number}')

    def fat(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Pai {n}')
        elif add != '':
            return self.ID(f'Pai {self.father_number + add}')
        elif reset:
            self.father_number = 0
        else:
            self.father_number += 1
            return self.ID(f'Pai {self.father_number}')
    
    def mot(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Mãe {n}')
        elif add != '':
            return self.ID(f'Mãe {self.mother_number + add}')
        elif reset:
            self.mother_number = 0
        else:
            self.mother_number += 1
            return self.ID(f'Mãe {self.mother_number}')
    
    def child(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Criança {n}')
        elif add != '':
            return self.ID(f'Criança {self.child_number + add}')
        elif reset:
            self.child_number = 0
        else:
            self.child_number += 1
            return self.ID(f'Criança {self.child_number}')
        
    def kids(self, n):
        return [self.child() for i in range(n)]
    
    def stu(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Estudante {n}')
        elif add != '':
            return self.ID(f'Estudante {self.student_number + add}')
        elif reset:
            self.student_number = 0
        else:
            self.student_number += 1
            return self.ID(f'Estudante {self.student_number}')
    
    def anim(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Animal {n}')
        elif add != '':
            return self.ID(f'Animal {self.animal_number + add}')
        elif reset:
            self.animal_number = 0
        else:
            self.animal_number += 1
            return self.ID(f'Animal {self.animal_number}')
        
    def mons(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Monstro {n}')
        elif add != '':
            return self.ID(f'Monstro {self.monster_number + add}')
        elif reset:
            self.monster_number = 0
        else:
            self.monster_number += 1
            return self.ID(f'Monstro {self.monster_number}')
        
    def dino(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Dinossauro {n}')
        elif add != '':
            return self.ID(f'Dinossauro {self.dino_number + add}')
        elif reset:
            self.dino_number = 0
        else:
            self.dino_number += 1
            return self.ID(f'Dinossauro {self.dino_number}')
        
    def cave(self, n = 0, add = '', reset = False):
        if n != 0:
            return self.ID(f'Homem das Cavernas {n}')
        elif add != '':
            return self.ID(f'Homem das Cavernas {self.caveman_number + add}')
        elif reset:
            self.caveman_number = 0
        else:
            self.caveman_number += 1
            return self.ID(f'Homem das Cavernas {self.caveman_number}')

    # Cria uma multidão, facilitando o acesso a muitos figurantes que se repetem em várias páginas
    def crowd(self, n = 0, name = '', reset = False, figs = 10, shades = 0, atts = 0, mots = 0, fats = 0, childs = 0, stus = 0, anims = 0,
             mons = 0, dinos = 0, caves = 0):
        if reset:
            self.crowd_number = 0
            self.list_crowds = []
        if n!= 0:
            return self.list_crowds[n-1]
        else:
            self.crowd_number += 1
            crowd = []
            if figs > 0:
                if name == '':
                    crowd += self.figs(figs)
                else:
                    num = 0
                    for c in self.list_crowds:
                        if name in c[0]:
                            num += len(c)
                    crowd += [self.ID(f'{name} {i}') for i in range(num+1, num+figs+1)]
            if shades > 0:
                crowd += self.shades(shades)
            if atts > 0:
                crowd += [self.att() for i in range(atts)]
            if mots > 0:
                crowd += [self.mot() for i in range(mots)]
            if fats > 0:
                crowd += [self.fat() for i in range(fats)]
            if childs > 0:
                crowd += [self.child() for i in range(childs)]
            if stus > 0:
                crowd += [self.stu() for i in range(stus)]
            if anims > 0:
                crowd += [self.anim() for i in range(anims)]
            if mons > 0:
                crowd += [self.mon() for i in range(mons)]
            if dinos > 0:
                crowd += [self.dino() for i in range(dinos)]
            if caves > 0:
                crowd += [self.cave() for i in range(caves)]
            self.list_crowds.append(crowd)
            return crowd
            
    
    def reset(self):
        self.fig(reset = True)
        self.shade(reset = True)
        self.att(reset = True)
        self.mot(reset = True)
        self.fat(reset = True)
        self.child(reset = True)
        self.stu(reset = True)
        self.anim(reset = True)
        self.mons(reset = True)
        self.dino(reset = True)
        self.cave(reset = True)
        self.crowd(reset = True)
