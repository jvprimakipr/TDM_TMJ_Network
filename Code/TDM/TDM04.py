from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm04'

pages4 = [[c.beg, c.cas, c.ceb, c.mon, 'Duende', c.cb + 'Múmia', c.end], # capa
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
          ['Duende', c.cb + 'Duende 2', c.cb + 'Duende 3', c.cb + 'Duende 4'],
          ['Duende', c.cb + 'Duende 2', c.cb + 'Duende 3', c.cb + 'Duende 4', c.cb + 'Duende 5', 'Papai Noel'],
          ['Duende', c.cb + 'Duende 2', c.cb + 'Duende 3', c.cb + 'Duende 4', c.cb + 'Duende 5', c.cb + 'Duende 6', c.cb + 'Duende 7', 'Papai Noel'],
          ['Duende', c.cb + 'Duende 2', c.cb + 'Duende 3', c.cb + 'Duende 4', c.cb + 'Duende 5', 'Papai Noel'],
          ['Duende', c.cb + 'Duende 2', c.cb + 'Duende 3', 'Papai Noel'],
          ['Papai Noel', c.cb + 'Rena 1', c.cb + 'Rena 2', c.cb + 'Rena 3', 'Duende', c.mon, c.ceb, c.cas, c.end], # fim da história
          [],
          [c.beg, c.cas],
          [c.cas, c.spa, c.anj, c.end], # fim da história
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
          [c.beg, c.cas, c.ceb, c.anim(), c.end], # fim da história
          [c.beg, c.chi, c.anim(), c.anim(), c.anim()],
          [c.chi, c.anim(), c.anim(), c.anim(), c.anim()],
          [c.chi, c.anim(), c.anim(), c.anim(), c.anim(), c.anim()],
          [c.chi, c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim()],
          [c.chi, c.ros, c.anim(), c.anim(), c.anim(), c.anim(), c.end], # fim da história
          [c.beg, c.pit, 'Gronk'],
          [c.pit, 'Gronk'],
          [c.pit, 'Gronk', c.end], # fim da história
          [],
          [c.beg, c.mon, c.ceb],
          [c.mon, c.ceb],
          [c.mon, c.ceb],
          [c.mon, c.ceb, c.end], # fim da história
          [c.beg, c.ceb, c.end]] # louco também? cebolinha vira o louco no último quadrinho (tirinha do final)
