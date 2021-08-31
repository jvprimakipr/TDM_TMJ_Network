from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#tdm_20') #Capa
his1 = [[c.beg, c.mon, c.ceb, c.mag, c.viv, c.end], [], [c.mon, c.ceb, c.mag, c.viv, c.san, c.bor], #1. A volta da Bruxa Viviane - Pág 3
        [c.beg, c.viv, c.bor], [c.viv, c.bor, c.mon, c.mag, c.ceb, c.cas],
        [c.viv, c.bor],
        [c.viv, c.bor],
        [c.viv, c.bor, c.att(), c.att()],
        [c.viv, c.bor, c.att(1)],
        [c.viv, c.bor, c.att(1)],
        [c.ceb, c.cas, c.viv, c.bor],
        [c.mon, c.ceb, c.cas, c.viv, c.bor],
        [c.mon, c.ceb, c.cas, c.viv, c.bor],
        [c.mon, c.ceb, c.cas, c.viv],
        [c.mon, c.ceb, c.cas, c.viv],
        [c.mon, c.ceb, c.cas, c.viv, c.bor],
        [c.mag, c.viv, c.bor, c.child()],
        [c.mag, c.viv, c.bor],
        [c.mag, c.viv, c.bor, c.shade(), c.att()],
        [c.mag, c.viv, c.att()],
        [2, [c.mag, c.viv, c.att(add=0)], [c.mon, c.ceb, c.mag, c.cas, c.viv]],
        [c.mon, c.ceb, c.mag, c.cas, c.viv],
        [c.mon, c.ceb, c.mag, c.cas, c.viv],
        [c.mon, c.ceb, c.mag, c.cas, c.viv, c.hor, c.mam, c.pte, c.bro],
        [c.mag, c.viv, c.mam, c.pte, c.bro, c.dino(), c.dino()],
        [c.mag, c.viv, c.bor],
        [c.mon, c.ceb, c.mag, c.cas, c.viv, c.bor,c.end],
        [],
        []]
his2 = [[c.beg, c.pit, c.anim()], #2. A rede  - Pág 30
        [c.pit],
        [c.pit, c.dino()],
        [c.pit, c.dino(add=0), c.end],
        [],
        [],
        [],
        []]
his3 = [[c.beg, c.pen, c.ID('Gato 1')], #3. O mesmo gato - Pág 38
        [c.pen, c.ID('Gato 1'), c.end]]
his4 = [[c.beg, c.ceb, c.floq], #4. Passeio... - Pág 40
        [c.ceb, c.floq, c.end]]
his5 = [[c.beg, c.dud, c.mdud], #5. Dudu, o policial galáctico - Pág 42
        [c.dud, 'Lactos Kid'],
        [c.dud, 'Lactos Kid', 'Milhus', 'Ervilhus'],
        [c.dud, 'Lactos Kid', 'Milhus', 'Ervilhus', 'Capitão Macarrônios', 'Monstro Q.I.Jo'] + c.crowd(name='Feijônico'),
        [c.dud, c.mdud, 'Lactos Kid', 'Milhus', 'Ervilhus'] + c.crowd(1)[:3] + [c.end],
        []]
his6 = [[2, [c.franj, c.bid], [c.ceb, c.bid], c.beg], #6. Ninguém me entende - Pág 48
        [2, [c.ceb, c.bid], [c.mon, c.cas, c.bid], c.end]]
his7 = [[c.beg, c.ast, c.ali(), c.ali()], #7. Cuidado onde pisa!
        [c.ast, c.ali(add = 0), c.ali(), c.end]]
his8 = [[c.beg, c.zlel, 'Odorica', c.fig(), c.fig(), c.att(), c.anim()], #8. Um dia no parque - Pág 52
        [2, [c.zlel, 'Odorica', c.att(add=0)] + c.kids(10), [c.zlel, 'Odorica', c.att()]],
        [2, [c.zlel, 'Odorica'] + c.kids(4), [c.zlel, c.mlel, 'Odorica'], c.end],
        []]
his9 = [[2, [c.lob] + c.anims(4), [c.lob, c.anim(add=-1), c.anim(add=0), c.child()], c.beg], #9. Bichinho de Estimação - Pág 56
        [c.lob, c.anim(add=-1), c.anim(add=0), c.child(), c.fig(), c.end]]
his10= [[2, [c.mon], [c.franj, c.bid], c.beg], #10. As Pegadas - Pág 58
        [2, [c.mag, c.min], [c.mon, c.ceb, c.floq], c.end]]
his11= [[c.beg, c.tin, c.pip], #11. Sorria, meu bem! - Pág 60
        [2, [c.tin, c.pip], [c.tin, c.ID('Serginho')]],
        [c.tin, c.pip, c.ID('Serginho')],
        [c.tin, c.pip],
        [c.tin, c.pip, c.ID('Serginho')],
        [c.tin, c.pip, c.ID('Serginho'), c.end]]
his12= [[c.beg, c.pen, c.zvam, c.mum, c.cra, c.end], #12. Tira final - Pág 66
        [],
        []]

pages1 = his1 + his2 + his3 + his4 + his5 + his6 + his7 + his8 + his9 + his10 + his11 + his12