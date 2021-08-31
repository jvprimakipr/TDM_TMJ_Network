from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#tdm_39') #Capa
his1 = [[c.beg, c.mon, c.ceb, c.cas, c.end], [], [c.beg, c.mon, c.ceb, c.cas], #1. O diário de Josefina - Pág 3
        ['Josefina'], ['Josefina'],
        [c.mon, c.ceb, c.cas, c.san, 'Josefina'],
        ['Josefina'],
        [c.mon, c.ceb, c.cas, c.san, c.pen, 'Josefina'],
        [c.mon, c.ceb, c.cas, c.zvam, 'Josefina'],
        [c.mon, c.cas, 'Josefina'],
        [c.mon, c.ceb, c.cas, 'Josefina'],
        [c.mon, c.ceb, c.cas, 'Josefina'],
        [c.mon, c.ceb, c.cas, 'Josefina', c.att()],
        [c.san, 'Josefina'],
        [c.mag, c.franj, c.xav, c.dud, c.jer],
        [c.mon, c.ceb, c.cas, c.san],
        [c.mon, c.ceb, c.cas, c.san],
        [c.mon, c.ceb, c.cas, c.san],
        [c.mon, c.ceb, c.cas, c.san, c.shade()],
        [c.mon, c.ceb, c.cas, c.san, c.shade()],
        [c.mon, c.ceb, c.cas, c.san],
        [c.mon, c.ceb, c.cas, c.san],
        [c.mon, c.ceb, c.cas, c.san],
        [c.mon, c.ceb, c.cas, c.san, c.end],
        []]
his2 = [[c.beg, c.pen, c.fra], #2. Posso ajudar? - Pág 26
        [c.pen, c.fra],
        [c.zvam, c.fra],
        [c.zvam, c.fra],
        [2, [c.zvam, c.fra], [c.fra, c.pix]],
        [c.fra, c.pix],
        [c.pen, c.fra, c.pix, c.end],
        [],
        [],
        [],
        [],
        []]
his3 = [[c.beg, c.mon, c.ceb, c.cas, c.xav, c.san, c.end]] #3. Pés - Pág 38
his4 = [[c.beg, c.pit, c.ogr, c.dino(), c.shade()], #4. O dia em que a Thuga viajou
        [c.pit, c.ogr],
        [c.pit] + c.crowd(figs=0, anims=3),
        [c.pit],
        [c.pit],
        [c.pit, c.thu],
        [c.pit, c.thu, c.ogr, c.end],
        []]
his5 = [[c.beg, c.ceb, c.cas], #5. Improviso - Pág 47
        [2, [c.ceb, c.cas], [c.mon, c.ceb]],
        [2, [c.ceb, c.cas], [c.mon, c.ceb]],
        [2, [c.mon, c.ceb], [c.ceb, c.cas]],
        [2, [c.ceb, c.cas], [c.mon, c.ceb]],
        [2, [c.ceb, c.cas], [c.mon, c.ceb]],
        [c.mon, c.ceb, c.cas],
        [c.mon, c.ceb, c.cas, c.san, c.end],
        []]
his6 = [[c.beg, c.lob, c.ID('Rex'), c.end]] #6. Turma do Penadinho - Pág 56
his7 = [[c.beg, c.mon, c.ceb, c.san], #7. Aula de desenho - Pág 57
        [c.mon, c.ceb, c.mar, c.san],
        [c.ceb, c.mar],
        [2, [c.mon, c.ceb], [c.ceb, c.mar]],
        [c.ceb, c.mar],
        [c.ceb, c.mar],
        [c.ceb, c.mar],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.mar, c.end]]
his8 = [[c.beg, c.rap, c.end],
        [],
        []]

pages20 = his1 + his2 + his3 + his4 + his5 + his6 + his7 + his8