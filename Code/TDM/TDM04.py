from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#tdm_23') #Capa
pages4 = [[c.beg, c.cas, c.ceb, c.mon, c.ID('Duende'), c.ID('Múmia'), c.end], # capa
          [],
          [c.mon], # introdução
          [c.beg, c.mon],
          [c.mon],
          [c.mon, c.ID('Duende'), c.mot(), c.fat(), c.mmon, c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()], # 19 crianças, 2 mães e 2 pais
          [c.mon, c.ID('Duende'), c.mmon],
          [c.mon, c.ID('Duende'), c.mmon],
          [c.mon, c.ID('Duende'), c.mmon, c.kid(), c.kid()],
          [c.ID('Duende'), c.att(), c.shade(), c.mot(), c.mot(), c.fat(), c.fat(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid()],
          [c.ID('Duende'), c.att(n = 1), c.mon, c.mmon, c.fat(), c.kid(), c.att()],
          [c.mon, c.mmon, c.ID('Duende')],
          [c.ID('Duende'), c.att(), c.att(), c.kid(), c.kid()],
          [c.ID('Duende'), c.mon],
          [c.ID('Duende'), c.mon, c.kid(), c.kid()],
          [c.ID('Duende'), c.mon, c.kid(), c.ceb, c.cas],
          [c.ID('Duende'), c.mon, c.ceb, c.cas],
          [c.ID('Duende'), c.kid(), c.ceb, c.cas],
          [c.ID('Duende'), c.mon, c.att(), c.ceb, c.cas],
          [c.ID('Duende'), c.mon, c.kid(), c.kid(), c.ceb, c.cas],
          [c.ID('Duende'), c.mon, c.ceb, c.cas],
          [c.ID('Duende'), c.mon, c.ceb, c.cas],
          [c.ID('Duende'), c.ID('Duende 2'), c.ID('Duende 3'), c.ID('Duende 4')],
          [c.ID('Duende'), c.ID('Duende 2'), c.ID('Duende 3'), c.ID('Duende 4'), c.ID('Duende 5'), 'Papai Noel'],
          [c.ID('Duende'), c.ID('Duende 2'), c.ID('Duende 3'), c.ID('Duende 4'), c.ID('Duende 5'), c.ID('Duende 6'), c.ID('Duende 7'), 'Papai Noel'],
          [c.ID('Duende'), c.ID('Duende 2'), c.ID('Duende 3'), c.ID('Duende 4'), c.ID('Duende 5'), 'Papai Noel'],
          [c.ID('Duende'), c.ID('Duende 2'), c.ID('Duende 3'), 'Papai Noel'],
          ['Papai Noel', c.ID('Rena 1'), c.ID('Rena 2'), c.ID('Rena 3'), c.ID('Duende'), c.mon, c.ceb, c.cas, c.end], # fim da história
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
