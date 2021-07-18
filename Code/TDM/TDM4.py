from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 4'

pages4 = [[c.beg, c.cas, c.ceb, c.mon, 'Duende', 'Múmia', c.end], # capa
          [],
          [c.mon], # introdução
          [c.beg, c.mon],
          [c.mon],
          [c.mon, 'Duende', c.mot(), c.fat(), c.mmon, c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()], # 19 crianças, 2 mães e 2 pais
          [c.mon, 'Duende', c.mmon],
          [c.mon, 'Duende', c.mmon],
          [c.mon, 'Duende', c.mmon, c.child(), c.child()],
          ['Duende', c.att(), c.shade(), c.mot(), c.mot(), c.fat(), c.fat(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          ['Duende', c.att(n = 1), c.mon, c.mmon, c.fat(), c.child(), c.att()],
          [c.mon, c.mmon, 'Duende'],
          ['Duende', c.att(), c.att(), c.child(), c.child()],
          ['Duende', c.mon],
          ['Duende', c.mon, c.child(), c.child()],
          ['Duende', c.mon, c.child(), c.ceb, c.cas],
          ['Duende', c.mon, c.ceb, c.cas],
          ['Duende', c.child(), c.ceb, c.cas],
          ['Duende', c.mon, c.att(), c.ceb, c.cas],
          ['Duende', c.mon, c.child(), c.child(), c.ceb, c.cas],
          ['Duende', c.mon, c.ceb, c.cas],
          ['Duende', c.mon, c.ceb, c.cas],
          ['Duende', 'Duende 2', 'Duende 3', 'Duende 4'],
          ['Duende', 'Duende 2', 'Duende 3', 'Duende 4', 'Duende 5', 'Papai Noel'],
          ['Duende', 'Duende 2', 'Duende 3', 'Duende 4', 'Duende 5', 'Duende 6', 'Duende 7', 'Papai Noel'],
          ['Duende', 'Duende 2', 'Duende 3', 'Duende 4', 'Duende 5', 'Papai Noel'],
          ['Duende', 'Duende 2', 'Duende 3', 'Papai Noel'],
          ['Papai Noel', 'Rena 1', 'Rena 2', 'Rena 3', 'Duende', c.mon, c.ceb, c.cas, c.end], # fim da história
          [],
          [c.beg, c.cas],
          [c.cas, 'São Paulo', 'Anjinho', c.end], # fim da história
          [c.beg, c.ceb, c.cas, c.mon, c.end], # fim da história
          [],
          [],
          [],
          [c.beg, c.min],
          [c.min, c.mag],
          [c.min, c.mag],
          [c.min, c.mag],
          [c.min, c.mag, c.mmag, c.end], # fim da história
          [c.beg, c.tv, c.mtv],
          [c.tv, c.mtv, c.blo], # a mãe tá só em voz
          [c.tv, c.mtv, c.blo],
          [c.tv, c.mtv, c.blo],
          [c.tv, c.mtv, c.blo],
          [c.tv, c.mtv, c.blo],
          [c.tv, c.mtv, c.blo],
          [c.tv, c.blo],
          [c.tv, c.mtv, c.blo, c.end], # fim da história
          [],
          [],
          [c.beg, c.cas, c.ceb, 'Enxame de abelhas', c.end], # fim da história
          [c.beg, c.chi, 'Galo', 'Cachorro', 'Lesma'],
          [c.chi, 'Tartaruga', 'Morcego', 'Formigas', 'Coruja'],
          [c.chi, 'Coelho', 'Macaco 1', 'Macaco 2', 'Preguiça', 'Cavalo'], # dois macacos
          ['Pato', c.chi, 'Mula', 'Porco', 'Gata', 'Gatinho 1', 'Gatinho 2', 'Gatinho 3'], # 3 filhotes de gato e a gata
          ['Bode 1', 'Bode 2', c.chi, c.ros, 'Pássaro 1', 'Pássaro 2', c.end], # dois bodes e dois pássaros / fim da história
          [c.beg, c.pit, 'Gronk'],
          [c.pit, 'Gronk'],
          [c.pit, 'Gronk', c.end], # fim da história
          [],
          [c.beg, c.mon, c.ceb],
          [c.mon, c.ceb],
          [c.mon, c.ceb],
          [c.mon, c.ceb, c.end], # fim da história
          [c.beg, c.ceb, c.end]] # louco também? cebolinha vira o louco no último quadrinho (tirinha do final)
