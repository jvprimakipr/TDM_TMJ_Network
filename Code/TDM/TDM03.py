from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#tdm_22') #Capa
his1 = [[c.beg, c.mon, c.ceb, c.cas, c.pceb, c.end], [], [c.ceb, c.pceb], #1. Acorda, meu!! - Pág 3
        [c.beg, c.ceb, c.pceb] + c.atts(2) + c.kids(4), [c.ceb, c.pceb, c.fat()] + c.kids(3),
        [2, [c.ceb, c.pceb, c.kid()], [c.ceb, c.pceb, c.att(), c.mot()] + c.kids(2)],
        [c.ceb, c.pceb] + c.kids(2),
        [c.ceb, c.pceb, c.kid(add=0)],
        [c.ceb, c.pceb, c.kid(add=0)],
        [c.ceb, c.pceb, c.att()],
        [c.ceb, c.pceb, c.kid()],
        [c.ceb, c.pceb] + c.kids(2),
        [c.ceb, c.pceb, c.kid(add=-1), c.kid(add=0)],
        [2, [c.ceb, c.pceb] + c.kids(2), [c.ceb, c.pceb] + c.kids(3)],
        [2, [c.ceb, c.pceb, c.kid()], [c.ceb, c.pceb] + c.kids(2)],
        [2, [c.ceb, c.pceb], [c.pceb, c.mot(), c.fat(), c.kid()]],
        [2, [c.pceb, c.fat(0), c.kid(0)], [c.ceb, c.pceb]],
        [2, [c.ceb, c.mceb, c.pceb] + c.crowd(figs=5, name='Jogador'), [c.pceb, c.fat(0), c.kid(0)]],
        [c.ceb, c.pceb],
        [c.ceb, c.pceb] + c.crowd(figs=2, name='Caramujo') + [c.end],
        []]
his2 = [[c.beg, c.mon, c.mag, c.san], #2. Paradinhos - Pág 22
        [c.ceb, c.mag, c.cas, c.xav, c.ID('Sorveteiro 1'), c.end]]
his3 = [[c.beg, c.cas, c.kid()] + c.figs(2), #3. Fazendo Compras - Pás 24
        [2, [c.cas] + c.figs(2), [c.cas] + c.figs(2)],
        [2, [c.cas, c.att()], [c.cas, c.mcas]],
        []]
his4 = [[c.beg, c.pit, c.var, c.dino()], #4. Saca só como surge um esporte!
        [c.pit, c.bol, c.var],
        [c.pit, c.bol, c.var],
        [c.pit, c.var, c.ID('Homem-Tigre 1')],
        [2, [c.pit, c.var, c.ID('Homem-Tigre 1')], [c.pit, c.bol, c.var, c.cave()]],
        [c.pit, c.bol, c.var] + [c.ID(f'Homem-Tigre {i}') for i in range(1,4)],
        [c.pit, c.bol, c.var] + c.caves(5),
        [2, [c.ID('Homem-Tigre 1'), c.ID('Homem-Tigre 3')], [c.pit, c.bol, c.var, c.cave(0)] + c.caves(2) + [c.ID(f'Homem-Tigre {i}') for i in range(1,6)], c.end]]
his5 = [[c.beg, c.zvam, c.kid(), c.end], #5. Batman - Pág 36
        [],
        [],
        []]
his6 = [[c.beg, c.pen] + c.figs(3), #6. Que tédio! Isto aqui parece um cemitério!
        [c.pen],
        [c.pen, c.fra],
        [c.pen, c.mum, c.zvam, c.fra, c.zcav],
        [c.pen, c.alm, c.mum, c.zvam, c.fra, c.zcav, c.lob, c.mor, c.ID('Fantasma 1'), c.ID('Fantasma 2'), c.end],
        []]
his7 = [[c.beg, c.mon, c.ceb, c.cas, c.san], #7. Troca - Pág 46
        [c.mon, c.ceb, c.cas, c.san, c.end]]
his8 = [[c.beg, c.pap, c.cai], #8. Nas terras do caiapopó - Pág 48
        [c.pap, c.cai, 'Onça'],
        [c.pap, c.cai, 'Onça'],
        [c.pap, c.cai, 'Onça', c.end]]
his9 = [[c.beg, c.zlel], #9. O Banho - Pág 52
        [c.zlel, c.end]]
his10= [[2, [c.ceb, c.san], [c.mon, c.ceb, c.san], c.beg], #10. Nós no Sansão - Pág 54
        [c.mon, c.ceb, c.san, c.end],
        []]
his11= [[c.beg, c.hum], #11. Aquele barulhinho da conchinha do mar - Pág 57
        [c.hum],
        [c.hum],
        [c.hum],
        [c.hum],
        [2, [c.hum, c.crowd()], [c.hum, c.fig()]],
        [c.hum],
        [c.hum, c.ID('Tritão 1')],
        [2, [c.hum, c.fat(), c.kid(), c.ID('Tritão 1')], [c.ID('Tritão 1'), c.ID('Tritão 2'), c.ID('Tritão 3')], c.end]]
his12= [[c.beg, c.pen, c.alm, c.zvam, c.end], #12. Tira final - Pág 66
        [],
        []]

pages3 = his1 + his2 + his3 + his4 + his5 + his6 + his7 + his8 + his9 + his10 + his11 + his12