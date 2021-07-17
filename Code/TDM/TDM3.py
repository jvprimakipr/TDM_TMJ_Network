from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 3'

pages3 = [[c.pceb, c.ceb, c.mon, c.cas], # capa
          [],
          [c.pceb, c.ceb], # introdução
          [c.ceb, c.pceb, c.att(), c.att(), c.child(), c.child(), c.child(), c.child()],
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
          [c.ceb, c.pceb, c.mot(), 'Bebê', c.fat()],
          [c.ceb, c.pceb, 'Bebê', c.fat(n = 2)],
          [c.ceb, c.pceb, 'Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4', 'Jogador 5', c.mceb, c.fat(n = 2), 'Bebê'],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb, 'Pai Caramujo', 'Filho Caramujo'], # fim da história
          [],
          [c.mon, c.san, c.mag],
          [c.ceb, c.mag, c.cas, c.xav, 'Sorveteiro'], # fim da história
          [c.cas, c.fig(), c.fig(), c.fig()],
          [c.cas, c.fig(), c.fig(), c.fig(), c.fig()],
          [c.cas, c.mcas, 'Caixa do Supermercado'], # fim da história
          [],
          [c.pit, c.var, 'Dinossauro Rosa'],
          [c.pit, c.var, c.bol],
          [c.pit, c.var, c.bol],
          [c.pit, c.var, 'Homem Tigre 1'],
          ['Homem Tigre 1', c.pit, c.var, c.bol, 'Homem das Cavernas 1'],
          [c.pit, c.var, c.bol, 'Homem Tigre 1', 'Homem Tigre 2', 'Homem Tigre 3'],
          [c.pit, c.var, c.bol, 'Homem das Cavernas 2', 'Homem das Cavernas 3', 'Homem das Cavernas 4', 'Homem das Cavernas 5', 'Homem das Cavernas 6'],
          ['Homem Tigre 1', 'Homem Tigre 2', 'Homem Tigre 3', 'Homem Tigre 4', 'Homem Tigre 5', c.pit, c.bol, c.var, 'Homem das Cavernas 1', 'Homem das Cavernas 2', 'Homem das Cavernas 3'], # fim da história
          [c.zvam, c.fig()], # fim da história
          [], # [c.ceb, c.cas, c.doc], # passatempo
          [], # [c.ceb, c.mon, c.cas, c.mag, c.marceb, c.xav, c.bid], # correio
          [], # [c.cas, c.ceb, c.mon, c.mag], # correio de novo
          [c.pen, c.fig(), c.fig(), c.fig()],
          [c.pen],
          [c.pen, c.fra],
          [c.pen, c.fra, c.zvam, c.mum, c.zcav],
          [c.pen, c.fra, c.zvam, c.mum, c.zcav, c.lob, c.mor, c.alm, 'Fantasma 1', 'Fantasma 2'], # fim da história
          [],
          [c.mon, c.ceb, c.cas, c.san],
          [c.mon, c.ceb, c.cas, c.san], # fim da história
          [c.pap, c.cai],
          [c.pap, c.cai, 'Onça'],
          [c.pap, c.cai, 'Onça'],
          [c.pap, c.cai, 'Onça'], # fim da história
          [c.zlel],
          [c.zlel], # fim da história
          [c.ceb, c.san, c.mon], # mônica só em pensamento
          [c.ceb, c.san, c.mon], # fim da história
          [],
          [c.hum],
          [c.hum],
          [c.hum],
          [c.hum],
          [c.hum, c.tar], # tarugo em pensamento
          [c.hum, 'Salva-vidas'], # tem um circo todo em pensamento
          [c.hum],
          [c.hum, 'Tritão 1'],
          [c.hum, c.fat(), c.child(), 'Tritão 1', 'Tritão 2', 'Tritão 3'], # fim da história
          [c.pen, c.alm, c.zvam]] # tirinha final
