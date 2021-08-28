from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm03'

pages3 = [[c.beg, c.pceb, c.ceb, c.mon, c.cas, c.end], # capa
          [],
          [c.pceb, c.ceb], # introdução
          [c.beg, c.ceb, c.pceb, c.att(), c.att(), c.child(), c.child(), c.child(), c.child()],
          [c.ceb, c.pceb, c.child(), c.child(), c.child(), c.fat()],
          [c.ceb, c.pceb, c.child(), c.child(), c.child(), c.mot(), c.att()],
          [c.ceb, c.pceb, c.child(), c.child()],
          [c.ceb, c.pceb, c.child(n = 12)],
          [c.ceb, c.pceb, c.child(n = 12)],
          [c.ceb, c.pceb, c.att()],
          [c.ceb, c.pceb, c.child()],
          [c.ceb, c.pceb, c.child(), c.child()],
          [c.ceb, c.pceb, c.child(n = 14), c.child(n = 15)],
          [c.ceb, c.pceb, c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.ceb, c.pceb, c.child(), c.child(), c.child()],
          [c.ceb, c.pceb, c.mot(), c.cb + 'Bebê', c.fat()],
          [c.ceb, c.pceb, c.cb + 'Bebê', c.fat(n = 2)],
          [c.ceb, c.pceb, c.cb + 'Jogador 1', c.cb + 'Jogador 2', c.cb + 'Jogador 3', c.cb + 'Jogador 4', c.cb + 'Jogador 5', c.mceb, c.fat(n = 2), c.cb + 'Bebê'],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb, c.anim(), c.anim(), c.end], # fim da história
          [],
          [c.beg, c.mon, c.san, c.mag],
          [c.ceb, c.mag, c.cas, c.xav, c.fig(), c.end], # fim da história
          [c.beg, c.cas, c.fig(), c.fig(), c.fig()],
          [c.cas, c.fig(), c.fig(), c.fig(), c.fig()],
          [c.cas, c.mcas, c.fig(), c.end], # fim da história
          [],
          [c.beg, c.pit, c.var, c.dino()],
          [c.pit, c.var, c.bol],
          [c.pit, c.var, c.bol],
          [c.pit, c.var, c.cave(n = 1)],
          [c.cave(n = 1), c.pit, c.var, c.bol, c.cave(n = 6)],
          [c.pit, c.var, c.bol, c.cave(n = 1), c.cave(n = 2), c.cave(n = 3)],
          [c.pit, c.var, c.bol, c.cave(n = 7), c.cave(n = 8), c.cave(n = 9), c.cave(n = 10), c.cave(n = 11)],
          [c.cave(n = 1), c.cave(n = 2), c.cave(n = 3), c.cave(n = 4), c.cave(n = 5), c.pit, c.bol, c.var, c.cave(n = 6), c.cave(n = 7), c.cave(n = 8), c.end], # fim da história
          [c.beg, c.zvam, c.fig(), c.end], # fim da história
          [], # [c.ceb, c.cas, c.doc], # passatempo
          [], # [c.ceb, c.mon, c.cas, c.mag, c.marceb, c.xav, c.bid], # correio
          [], # [c.cas, c.ceb, c.mon, c.mag], # correio de novo
          [c.beg, c.pen, c.fig(), c.fig(), c.fig()],
          [c.pen],
          [c.pen, c.fra],
          [c.pen, c.fra, c.zvam, c.mum, c.zcav],
          [c.pen, c.fra, c.zvam, c.mum, c.zcav, c.lob, c.mor, c.alm, c.cb + 'Fantasma 1', c.cb + 'Fantasma 2', c.end], # fim da história
          [],
          [c.beg, c.mon, c.ceb, c.cas, c.san],
          [c.mon, c.ceb, c.cas, c.san, c.end], # fim da história
          [c.beg, c.pap, c.cai],
          [c.pap, c.cai, 'Onça'],
          [c.pap, c.cai, 'Onça'],
          [c.pap, c.cai, 'Onça', c.end], # fim da história
          [c.beg, c.zlel],
          [c.zlel, c.end], # fim da história
          [c.beg, c.ceb, c.san, c.mon], # mônica só em pensamento
          [c.ceb, c.san, c.mon, c.end], # fim da história
          [],
          [c.beg, c.hum],
          [c.hum],
          [c.hum],
          [c.hum],
          [c.hum, c.tar], # tarugo em pensamento
          [c.hum, c.fig(), c.crowd()], # tem um circo todo em pensamento (chamei de multidão, mas não sei quantos caras aparecem)
          [c.hum],
          [c.hum, c.cb + 'Tritão 1'],
          [c.hum, c.fat(), c.child(), c.cb + 'Tritão 1', c.cb + 'Tritão 2', c.cb + 'Tritão 3', c.end], # fim da história
          [c.beg, c.pen, c.alm, c.zvam, c.end]] # tirinha final
