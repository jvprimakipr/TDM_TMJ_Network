from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#tdm_21') #Capa
his1 = [[c.beg, c.mag, 'Dud Van Winkle', c.child(), c.end], [], [c.beg, c.mag, c.dud], #1. Dud Van Winkle - Pág 3
        [c.mag, c.dud], [c.mag, c.dud],
        [c.mag, c.dud, c.child()],
        [2, ['Dud Van Winkle'] + c.figs(2) + c.anims(5), [c.mag, c.dud]],
        [2, [c.mag, c.dud], ['Dud Van Winkle', c.fig()]],
        ['Dud Van Winkle'] + c.anims(4),
        [2, [c.mag, c.dud], ['Dud Van Winkle', c.anim()]],
        ['Dud Van Winkle'],
        [2, [c.mag, c.dud], [] + c.figs(3)],
        [2, [c.fig(add=-1), c.fig(add=0)], [c.child(), c.mot()]],
        [c.mau, 'Dud Van Winkle', c.fig()],
        [c.mau, 'Dud Van Winkle'],
        [2, ['Dud Van Winkle'], [c.mag, c.dud]],
        [2, [c.mag, c.dud], [c.dud, c.pen]],
        [2, [c.mag, c.dud, c.mau], [c.mau, 'Dud Van Winkle'], c.end],
        []]
his2 = [[c.beg, c.cas], #2. Brinquedo novo - Pág 20
        [c.cas, c.end]]
his3 = [[c.beg, c.mon, c.ceb, c.mag, c.san], # 3. Assim, não dá! - Pág 22
        [c.mon, c.mag, c.cas, c.san],
        [c.mon, c.mag, c.xav, c.san, c.end]]
his4 = [[c.beg, c.moca, c.min], #4. Experiências Frufrus - Pág 25
        [c.mon, c.mag, c.san, c.moca, c.floq, c.min, c.chov, c.rad],
        [c.franj, c.moca, c.floq, c.min, c.chov, c.bid, c.rad, c.end]]
his5 = [[c.beg,  c.zvam, c.lob], #5. Pum! - Pág 28
        [c.pen,  c.mum, c.zvam, c.fra, c.end]]
his6 = [[c.beg, c.mon, c.mag, c.mar, c.fig(), c.end], #6. Na praia - Pág 30
        []]
his7 = [[c.beg, c.mon, c.ceb, c.cas, c.tit, 'Super Homão', c.end], #7. Turma da Mônica - Pág 32
        [],
        [],
        []]
his8 = [[c.beg, c.pit] + c.crowd(figs=0, caves=2), #8. Inventei a roda! - Pág 36
        [c.pit] + c.crowd(1),
        [c.pit] + c.crowd(1),
        [c.pit, c.anim(), c.dino()],
        [c.pit, c.bol, c.cave(), c.end],
        []]
his9 = [[c.beg, c.dud], #9. O caçador dos brocólis perdidos - Pág 42
        [c.dud],
        [c.dud, c.mdud, c.end]]
his10= [[c.beg, c.mag, c.franj], #10. Um dia enrolado - Pág 45
        [c.mag, c.franj],
        [c.mag, c.franj],
        [c.franj],
        [c.mag, c.franj],
        [c.mag, c.franj],
        [c.mag, c.franj, c.end]]
his11= [[c.beg, c.mag, c.mmag], #11. Hora da bóia - Pág 52
        [c.mag, 'Anjo da Guarda da Magali', c.end],
        []]
his12= [[c.beg, c.bid, c.ped], #12. Bidugital - Pág 55
        [c.bid, c.ped, c.manf],
        [c.bid, c.manf] + c.crowd(figs=3, name='Desenhista'),
        [c.bid, c.manf, c.ped],
        [c.bid, c.manf, c.ped],
        [c.bid, c.manf, c.ped],
        [c.bid, c.manf, c.ped],
        [c.bid, c.manf, c.ped],
        [c.bid, c.manf, c.ped],
        [c.bid, c.manf] + c.crowd(2),
        [2, [c.bid, c.manf] + c.crowd(2), [c.bid, c.ped], c.end]]
his13= [[c.beg, c.lob, c.end], #13. Tira final - Pág 66
        [],
        []]

pages2 = his1 + his2 + his3 + his4 + his5 + his6 + his7 + his8 + his9 + his10 + his11 + his12 + his13