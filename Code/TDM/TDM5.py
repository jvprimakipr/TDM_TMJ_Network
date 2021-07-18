from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 5'

pages5 = [[c.beg, 'Homem Invisível', 'Mulher Invisível', c.cra, c.zcav, c.fra, c.lob, c.zvam, c.mum, c.pen, c.end],
          [],
          [c.pen],
          [c.beg, c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.fig()],
          [c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.mag, c.att(), c.att(), c.shade(), c.shade(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.pen, c.cra],
          ['Funcionário Parque', c.pen],
          [c.zvam, c.mum, c.fra, c.lob, c.cra, c.pen, c.zcav, 'Camisa 1', 'Camisa 2', 'Camisa 3', 'Vestido', 'Lixo'],
          [c.zvam, c.mum, c.fra, c.lob, c.cra, c.pen, c.zcav, 'Vestido', c.alm, 'Toalha', 'Lixo', 'Fantasminha'],
          [c.zvam, c.fra, c.cra, c.pen, 'Vestido', c.alm, 'Lixo', 'Fantasminha'],
          [c.zvam, c.lob, c.cra, c.pen, 'Vestido', c.alm, 'Toalha', 'Camisa 1', 'Camisa 2', 'Camisa 3', 'Fantasminha'],
          [c.fra, c.lob, c.cra, c.zcav, c.pen, 'Vestido', c.alm, 'Toalha', 'Lixo', 'Camisa 1', 'Camisa 2', 'Camisa 3', 'Fantasminha'],
          ['Guarda', c.zcav, c.pen, 'Vestido', 'Toalha', 'Lixo', 'Camisa 1', 'Camisa 2', 'Camisa 3', c.end], # fim da história
          [c.beg, c.cas],
          [c.cas, c.mcas, c.end], # fim da história
          [c.beg, c.mon, c.mar, c.bid], # Bidu só em fala
          [c.mon, c.mar, c.bid],
          [c.mon, c.mar, c.floq],
          [c.mon, c.mar, c.moca, 'Labrador', 'Cachorro Branco', 'Pitbull'],
          [c.mon, c.mar, c.ceb, c.san, c.end], # fim da história
          [],
          [],
          [c.beg, c.mceb, c.ceb, 'Anjinho', 'Anjinho 2', 'Anjinho 3', 'Anjinho 4', 'Anjinho 5', c.end], # fim da história
          [c.beg, c.chi, 'Galo'],
          [c.chi, 'Galo', c.end], # fim da história
          [c.beg, c.mau, 'Desenhista 1', 'Desenhista 2', 'Desenhista 3', 'Desenhista 4', c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mau, 'Desenhista 1', 'Desenhista 2', 'Desenhista 3', 'Desenhista 4', 'Tina', c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()], # fim da história
          [c.naj, c.jot, 'Formiga', c.end], # fim da história
          [], # [c.dud, c.cas, 'Anjinho', c.franj, c.mon], # passatempos
          [], # [c.mon, c.mag, c.cas, c.ceb, c.bid, c.xav, c.pen], # correio
          [], # [c.mon, c.mag, c.chi, c.nim, c.cas], # tem três meninas que não conheço (correio)
          [c.beg, c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra, 'Doutor'],
          [c.lob, c.pen, c.fra, 'Doutor'],
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra, c.end], # fim da história
          [],
          [c.beg, c.ceb, c.floq],
          [c.ceb, c.floq, c.end], # fim da história
          [c.beg, c.ast],
          [c.ast],
          [c.ast],
          [], # só aparece a nave do astronauta
          [c.ast],
          [c.ast],
          [c.ast, 'Astronauta do Futuro'],
          [c.ast, 'Astronauta do Futuro'],
          [c.ast, c.mast, c.past, c.end], # fim da história
          [],
          [c.beg, c.zcav, 'Cachorro', c.end], # fim da história
          [c.beg, c.ceb, c.san],
          [c.ceb, c.san, c.moca],
          [c.ceb, c.san, c.moca],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon, c.cas, c.end], # fim da história
          [c.beg, c.pen, c.alm, c.end]] # tirinha do final
