from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm02'
c.cb = c.comic_book + ' '

pages2 = [[c.beg, c.mag, 'Dud Van Winkle', c.fig(), c.end], # capa (Dud parece o Dudu)
          [],
          [c.mag, c.dud],
          [c.beg, c.mag, c.dud],
          [c.mag, c.dud],
          [c.mag, c.dud, c.fig()],
          ['Mulher - História', 'Homem - História', c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.dud, 'Dud Van Winkle'],
          [c.mag, c.dud, 'Dud Van Winkle', 'Vovó - História'],
          ['Dud Van Winkle', c.anim(), c.anim(), c.anim(), c.anim()],
          [c.mag, c.dud, 'Dud Van Winkle'],
          ['Dud Van Winkle'],
          [c.dud, c.mag, c.fig(), c.fig(), c.fig()],
          [c.fig(), c.fig(), c.child(), c.mot()],
          [c.mau, 'Dud Van Winkle', c.fig()],
          [c.mau, 'Dud Van Winkle'],
          ['Dud Van Winkle', c.dud, c.mag],
          [c.dud, c.mag, c.pen], # penadinho era num brinquedo
          [c.dud, c.mag, c.mau, 'Dud Van Winkle', c.end], # fim da história
          [],
          [c.beg, c.cas],
          [c.cas, c.end], # fim da história
          [c.beg, c.ceb, c.mon, c.mag, c.san],
          [c.cas, c.mon, c.mag, c.san],
          [c.mon, c.mag, c.san, c.xav, c.end], # fim da história
          [c.beg, c.moca, c.min],
          [c.mon, c.mag, c.san, c.moca, c.min, c.chov, c.floq, c.anim()],
          [c.franj, c.bid, c.moca, c.min, c.chov, c.floq, c.anim(add = 0), c.end], # fim da história
          [c.lob, c.zvam],
          [c.zvam, c.pen, c.fra, c.mum, c.end], # fim da história
          [c.beg, c.mon, c.mag, c.mar, c.fig(), c.end], # fim da história
          [],
          [c.beg, c.mon, c.ceb, c.tit, 'Super Homem', c.cas, c.end], # fim da história
          [],
          [],
          [],
          [c.beg, c.pit, c.cave(), c.cave()],
          [c.pit, c.cave(add = -1), c.cave(add = 0)],
          [c.pit, c.cave(add = -1), c.cave(add = 0)],
          [c.pit, c.dino(), c.dino()],
          [c.pit, c.cave(), c.cave(), c.end], # fim da história
          [],
          [c.beg, c.dud],
          [c.dud],
          [c.dud, c.mdud, c.end], # fim da história
          [c.beg, c.mag, c.franj],
          [c.mag, c.franj],
          [c.mag, c.franj],
          [c.franj],
          [c.mag, c.franj],
          [c.mag, c.franj],
          [c.mag, c.franj, c.end], # fim da história
          [c.beg, c.mag, c.mmag], # acho que ela quem chama a magali para casa (não aparece, só o balão de voz)
          [c.mag, 'Anjo da Guarda da Magali', c.end], # fim da história
          [],
          [c.beg, c.bid, c.cb + 'Pedra'], # a pedra fala!!!
          [c.bid, c.cb + 'Pedra', c.manf],
          [c.bid, c.manf, c.cb + 'Desenhista 1', c.cb + 'Desenhista 2', c.cb + 'Desenhista 3'],
          [c.bid, c.manf, c.cb + 'Pedra'],
          [c.bid, c.cb + 'Pedra', c.manf],
          [c.bid, c.manf, c.cb + 'Pedra'],
          [c.bid, c.manf, c.cb + 'Pedra'],
          [c.bid, c.manf, c.cb + 'Pedra'],
          [c.bid, c.manf, c.cb + 'Pedra'],
          [c.bid, c.manf, c.cb + 'Desenhista 1', c.cb + 'Desenhista 2', c.cb + 'Desenhista 3'],
          [c.beg, c.bid, c.manf, c.cb + 'Desenhista 1', c.cb + 'Desenhista 2', c.cb + 'Desenhista 3', c.cb + 'Pedra', c.end]] # fim da história
