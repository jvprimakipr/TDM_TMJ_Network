from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 5'

pages5 = [['Homem Invisível', 'Mulher Invisível', c.cra, c.zcav, c.fra, c.lob, c.zvam, c.mum, c.pen],
          [],
          [c.pen],
          [c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.fig()],
          [c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.mag, c.att(), c.att(), c.shade(), c.shade(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()], # e mais 10 crianças...
          [c.pen, c.cra],
          ['Funcionário Parque', c.pen],
          [c.zvam, c.mum, c.fra, c.lob, c.cra, c.pen, c.zcav, 'Camisa 1', 'Camisa 2', 'Camisa 3', 'Vestido', 'Lixo'],
          [c.zvam, c.mum, c.fra, c.lob, c.cra, c.pen, c.zcav, 'Vestido', c.alm, 'Toalha', 'Lixo', 'Fantasminha'],
          [c.zvam, c.fra, c.cra, c.pen, 'Vestido', c.alm, 'Lixo', 'Fantasminha'],
          [c.zvam, c.lob, c.cra, c.pen, 'Vestido', c.alm, 'Toalha', 'Camisa 1', 'Camisa 2', 'Camisa 3', 'Fantasminha'],
          [c.fra, c.lob, c.cra, c.zcav, c.pen, 'Vestido', c.alm, 'Toalha', 'Lixo', 'Camisa 1', 'Camisa 2', 'Camisa 3', 'Fantasminha'],
          ['Guarda', c.zcav, c.pen, 'Vestido', 'Toalha', 'Lixo', 'Camisa 1', 'Camisa 2', 'Camisa 3'], # fim da história
          [c.cas],
          [c.cas, c.mcas], # fim da história
          [c.mon, c.mar, c.bid], # Bidu só em fala
          [c.mon, c.mar, c.bid],
          [c.mon, c.mar, c.floq],
          [c.mon, c.mar, c.moca, 'Labrador', 'Cachorro Branco', 'Pitbull'],
          [c.mon, c.mar, c.ceb, c.san], # fim da história
          [],
          [],
          [c.mceb, c.ceb, 'Anjinho', 'Anjinho 2', 'Anjinho 3', 'Anjinho 4', 'Anjinho 5'], # fim da história
          [c.chi, 'Galo'],
          [c.chi, 'Galo'], # fim da história
          [c.mau, 'Desenhista 1', 'Desenhista 2', 'Desenhista 3', 'Desenhista 4', c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mau, 'Desenhista 1', 'Desenhista 2', 'Desenhista 3', 'Desenhista 4', 'Tina', c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()], # fim da história
          [c.naj, c.jot, 'Formiga'], # fim da história
          [], # [c.dud, c.cas, 'Anjinho', c.franj, c.mon], # passatempos
          [], # [c.mon, c.mag, c.cas, c.ceb, c.bid, c.xav, c.pen], # correio
          [], # [c.mon, c.mag, c.chi, c.nim, c.cas], # tem três meninas que não conheço (correio)
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra, 'Doutor'],
          [c.lob, c.pen, c.fra, 'Doutor'],
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra], # fim da história
          [],
          [c.ceb, c.floq],
          [c.ceb, c.floq], # fim da história
          [c.ast],
          [c.ast],
          [c.ast],
          [], # só aparece a nave do astronauta
          [c.ast],
          [c.ast],
          [c.ast, 'Astronauta do Futuro'],
          [c.ast, 'Astronauta do Futuro'],
          [c.ast, c.mast, c.past], # fim da história
          [],
          [c.zcav, 'Cachorro'], # fim da história
          [c.ceb, c.san],
          [c.ceb, c.san, c.moca],
          [c.ceb, c.san, c.moca],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon],
          [c.ceb, c.san, c.moca, c.mon, c.cas], # fim da história
          [c.pen, c.alm]] # tirinha do final
