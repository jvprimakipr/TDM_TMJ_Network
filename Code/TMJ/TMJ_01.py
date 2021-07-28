from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '1tmj_01'

cap1 = [[c.beg, c.mon, c.ceb, c.mag, c.cas, c.yuk, 'Kraker', c.end], #capa
        #[],
        #[],
        #[],
        #[],
        #[],
        [c.beg, c.mon, c.mmon, c.san], #Página 7
        [c.mon, c.san],
        [c.mon, c.san],
        [c.mon],
        [c.mon, c.pmon, c.san],
        [c.mon, c.pmon, c.san],
        [c.mon, c.pmon],
        [c.mon, c.pmon],
        [c.cas, c.mcas, c.pcas],
        [c.cas, c.pcas],
        [c.cas, c.pcas],
        [c.cas, c.pcas, c.ceb], #[1/4, [c.cas, c.pcas], [c.ceb]]
        [c.ceb, c.pceb, c.marceb],
        [c.ceb, c.mceb, c.marceb],
        [c.ceb, c.mceb, c.marceb],
        [c.ceb, c.marceb, c.mon],
        [c.mag, c.pmag, c.min, c.ave],
        [c.mag, c.mmag, c.pmag],
        [c.mon, c.mmon],
        [c.mmon, c.yuk],
        [c.mon, c.mmon],
        [c.mon, c.mmon],
        [c.mon, c.mmon, c.mag],
        [c.mon, c.pmon, c.mag],
        [c.mmon, c.pcas],
        [c.cas],
        [c.ceb, c.marceb, c.cas],
        [c.ceb, c.cas],
        [c.ceb, c.marceb, c.cas],
        [c.ceb, c.cas, c.mar],
        [c.ceb, c.cas],
        [c.ceb, c.cas],
        [c.ceb, c.cas, c.mon, c.pmon, c.mag], #[1/2, [c.ceb, c.cas], [c.mon, c.pmon, c.mag]]
        [c.mon, c.pmon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.end]
       ]#[],
cap2 = [[c.beg, c.franj, c.fal, 'Robô de Boas Vindas', 'Entregador'],
        [c.franj, c.fal, 'Robô de Boas Vindas', 'Entregador'],
        [c.franj, c.fal],
        [c.franj, 'Entregador'],
        [c.franj, 'Entregador'],
        [c.franj, 'Entregador'],
        [c.franj],
        [c.franj, c.anj],
        [c.mon, c.cas],
        [c.mon, c.ceb, c.lou],
        [c.mon, c.ceb, c.cas, c.lou],
        [c.franj, c.anj],
        [c.franj, c.anj, c.fal],
        [c.franj, c.fal],
        [c.franj, c.anj, c.fal],
        [c.cap, c.fal],
        [c.franj, c.anj, c.fal, c.cap, 'Dragão de Poeira'],
        [c.franj, c.anj, c.fal, c.cap, 'Dragão de Poeira'],
        [c.franj, c.anj, c.fal, c.cap],
        [c.cap, c.fal, 'Monstro de Poeira 1'],
        [c.cap, 'Monstro de Poeira 1', 'Monstro de Poeira 2'],
        [c.franj, c.anj],
        [c.cap, 'Dragão de Poeira'],
        [c.anj, 'Dragão de Poeira'],
        [c.franj, c.fal, 'Monstro de Poeira 1'],
        [c.franj, c.cap, c.fal, 'Monstro de Poeira 1'],
        [c.cap, c.fal],
        [c.cap],
        [c.franj, c.cap, c.fal, 'Monstro de Poeira 1', 'Monstro de Poeira 2'],
        [c.franj, c.cap, c.fal, 'Monstro de Poeira 1', 'Monstro de Poeira 2'],
        [c.mon, c.cas, c.lou],
        [c.mon, c.franj],
        [c.mon, c.ceb, c.franj],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas, c.cap],
        [c.mon, c.ceb, c.mag, c.franj, c.cap, 'Monstro de Poeira 1'],
        [c.cas, c.cap],
        [c.mon, c.ceb, c.cap],
        [c.mon, c.ceb, c.mag, c.cas, c.yuk, c.end]]
cap3 = [[c.beg, c.mon, c.ceb, c.mag, c.cas, c.yuk],
        [c.mon, c.ceb, c.mag, c.cas, c.yuk],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.cap],
        [c.mon, c.ceb, c.mag, c.cas, c.cap, c.yuk],
        [c.mon, c.ceb, c.mag, c.cas, c.cap, c.yuk],
        [c.cap, c.yuk],
        [c.mon, c.ceb, c.mag, c.cas, c.mmon, c.pceb, c.mmag, c.pcas],
        [c.mon, c.ceb, c.mag, c.cas, c.yuk],
        [c.cap, c.pceb],
        [c.mmon, c.pceb, c.mmag, c.pcas, c.fig(), 'Cavalo 1', 'Cavalo 2', 'Cavalo 3', 'Cavalo 4'],
        [c.mmon, c.pceb, c.mmag, c.pcas, 'Imperador', 'Guarda 1', 'Guarda 2'],
        [c.mmon, c.pceb, c.mmag, c.pcas, c.yuk, 'Imperador', 'Guarda 2'],
        [c.mmon, c.pceb, c.mmag, c.pcas, 'Imperador'],
        [c.ceb, 'Imperador'],
        [c.mmon, c.pceb, c.mmag, c.pcas, 'Imperador'],
        [c.mmon, c.pceb, c.mmag, c.pcas, c.ebor, c.ezep, c.eeur, c.enot, 'Imperador'],
        [c.mmon, c.pceb, c.mmag, c.pcas, c.ebor, c.ezep, c.eeur, c.enot],
        [c.mmon, c.pceb, c.pcas, 'Cavalo 1', 'Cavalo 2', 'Cavalo 4'],
        [c.mmag, c.yuk, 'Cavalo 3'],
        [c.mon, c.ceb, c.cas, c.mmon],
        [c.cap, c.yuk],
        [c.mon, c.ceb, c.cap, c.ebor, c.ezep, c.eeur, c.enot],
        [c.ceb, c.cap, c.franj, c.ebor, c.ezep, c.eeur, c.enot, 'Monstro de Poeira 1'],
        [c.mon, c.ceb, c.mag, c.cas, c.cap],
        [c.mon, c.cap, c.yuk],
        [c.yuk, c.ebor, c.ezep, c.eeur, c.enot],
        [c.mon, c.ceb, c.mag, c.cas, c.mmon, c.pceb, c.yuk],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.yuk, c.ebor, c.ezep, c.eeur, c.enot],
        [c.mon, c.mmon, c.pceb, c.mmag, c.pcas, c.yuk],
        [c.mon, c.mmon],
        [c.ceb, c.mag, c.cas, c.cap],
        [c.franj, c.fal, c.yuk, 'Monstro de Poeira 1', 'Monstro de Poeira 2'],
        [c.mon, c.ceb, c.mag, c.cas, c.ebor, c.ezep, c.eeur, c.enot],
        [c.ark, 'Kraker', 'Ninja', 'Lobisomem'],
        [c.mon, c.ceb, c.mag, c.cas, c.cap],
        [c.mon, c.yuk],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas, c.yuk, c.end],
        #[],
        #[],
        #[],
        #[],
        [c.mon, c.ceb]] #4º Capa
        
pages1 = cap1 + cap2 + cap3