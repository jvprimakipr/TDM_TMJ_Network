from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#tdm_38') #Capa
his1 = [[c.beg, c.mon, c.ceb, c.anj, 'Jonas (cadeirante)', c.end], [], [c.mon, c.ceb] + c.crowd(figs=0, childs=10) + c.shades(10), #Intro
        [c.beg, c.mon, 'João (irmão de Jonas)'], [c.mon, c.ceb, c.san], #1. Se Jonas não vai ao parque... - Pág 4
        [c.mon, c.ceb, c.san],
        [c.mon, c.ceb, c.san],
        [2, [c.anj, c.san, c.ID('Anjo 1')], [c.mon, c.ceb, c.anj, c.san]],
        [c.mon, c.ceb, c.anj, c.san],
        [c.mon, c.ceb, c.anj, c.san],
        [c.mon, c.ceb, c.anj, 'Anjoteque'],
        [c.mon, c.ceb, c.anj, 'Anjoteque'],
        [c.mon, c.ceb, c.anj, 'Anjoteque'],
        [c.mon, c.ceb, c.anj],
        [c.mon, c.ceb, c.anj],
        [c.mon, c.ceb, c.anj],
        [c.mon, c.ceb, c.anj],
        [c.mon, c.ceb, c.anj, 'Anjoteque'],
        [c.mon, c.ceb, c.anj],
        [c.anj, 'Anjoteque', 'Jonas (cadeirante)', 'João (irmão de Jonas)'],
        [c.mon, c.ceb, c.anj, 'Jonas (cadeirante)', 'João (irmão de Jonas)'],
        [c.mon, c.ceb, c.anj, 'Anjoteque', 'Jonas (cadeirante)', 'João (irmão de Jonas)', c.ID('Anjo 2'), c.ID('Anjo 3')],
        ['Jonas (cadeirante)'],
        ['Jonas (cadeirante)', 'João (irmão de Jonas)'],
        [c.zcav, 'Jonas (cadeirante)', 'João (irmão de Jonas)'],
        [c.anj, 'Jonas (cadeirante)', 'João (irmão de Jonas)'],
        [c.mon, c.ceb, c.anj, 'Anjoteque', 'Jonas (cadeirante)', 'João (irmão de Jonas)'],
        [c.mon, c.ceb, c.anj, c.end],
        []]
his2 = [[c.beg, c.franj, c.bid, c.end]] #2. Franjinha - Pág 30
his3 = [[c.beg, c.pit, c.dino()], #3. A Maldição - Pág 31
        [c.pit, c.dino()],
        [c.pit, c.bol],
        [c.pit, c.bol],
        [c.pit, c.dino(), c.dino()],
        [c.pit, c.ID('Sábio da Montanha')],
        [c.pit, c.ID('Sábio da Montanha')],
        [2, [c.pit, c.dino(0)], [c.pit, c.dino()], c.end],
        [],
        [],
        [],
        [],
        []]
his4 = [[c.beg, c.xav, c.pxav], #4. Fazendo a barba com o papai - Pág 44
        [c.xav, c.pxav],
        [c.xav, c.pxav],
        [c.xav, c.pxav],
        [c.xav, c.pxav],
        [c.xav, c.pxav],
        [c.xav, c.pxav],
        [c.xav, c.pxav],
        [c.xav, c.pxav] + c.crowd(figs=4, name='Bombeiro'),
        [2, [c.xav, c.pxav], [c.xav, c.xab, c.mxav], c.end]]
his5 = [[c.beg, c.pit, c.thu, c.dino(), c.end], #5. Caverninha - Pág 54
        []]
his6 = [[c.beg, c.ceb, c.cas], #6. Jogo Perigoso - Pág 56
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas, c.end]]
his7 = [[c.beg, c.pen, c.end], #7. Tira Final - Pág 66
        [],
        []]

pages19 = his1 + his2 + his3 + his4 + his5 + his6 + his7
