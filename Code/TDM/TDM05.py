from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#tdm_24') #Capa
pages5 = [[c.beg, 'Homem Invisível', 'Mulher Invisível', c.cra, c.zcav, c.fra, c.lob, c.zvam, c.mum, c.pen, c.end],
          [],
          [c.pen],
          [c.beg, c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid()],
          [c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid()],
          [c.kid(), c.kid(), c.kid(), c.kid(), c.kid()],
          [c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.fig()],
          [c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid()],
          [c.mag, c.att(), c.att(), c.shade(), c.shade(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid(), c.kid()],
          [c.pen, c.cra],
          [c.fig(), c.pen],
          [c.zvam, c.mum, c.fra, c.lob, c.cra, c.pen, c.zcav, c.ID('Camisa 1'), c.ID('Camisa 2'), c.ID('Camisa 3'), c.ID('Vestido'), c.ID('Lixo')],
          [c.zvam, c.mum, c.fra, c.lob, c.cra, c.pen, c.zcav, c.ID('Vestido'), c.alm, c.ID('Toalha'), c.ID('Lixo'), c.ID('Fantasminha')],
          [c.zvam, c.fra, c.cra, c.pen, c.ID('Vestido'), c.alm, c.ID('Lixo'), c.ID('Fantasminha')],
          [c.zvam, c.lob, c.cra, c.pen, c.ID('Vestido'), c.alm, c.ID('Toalha'), c.ID('Camisa 1'), c.ID('Camisa 2'), c.ID('Camisa 3'), c.ID('Fantasminha')],
          [c.fra, c.lob, c.cra, c.zcav, c.pen, c.ID('Vestido'), c.alm, c.ID('Toalha'), c.ID('Lixo'), c.ID('Camisa 1'), c.ID('Camisa 2'), c.ID('Camisa 3'), c.ID('Fantasminha')],
          [c.fig(), c.zcav, c.pen, c.ID('Vestido'), c.ID('Toalha'), c.ID('Lixo'), c.ID('Camisa 1'), c.ID('Camisa 2'), c.ID('Camisa 3'), c.end], # fim da história
          [c.beg, c.cas],
          [c.cas, c.mcas, c.end], # fim da história
          [c.beg, c.mon, c.mar, c.bid], # Bidu só em fala
          [c.mon, c.mar, c.bid],
          [c.mon, c.mar, c.floq],
          [c.mon, c.mar, c.moca, c.anim(), c.anim(), c.anim()],
          [c.mon, c.mar, c.ceb, c.san, c.end], # fim da histór)ia
          [],
          [],
          [c.beg, c.mceb, c.ceb, c.anj, c.ID('Anjinho 2'), c.ID('Anjinho 3'), c.ID('Anjinho 4'), c.ID('Anjinho 1'), c.end], # fim da história
          [c.beg, c.chi, c.anim()],
          [c.chi, c.anim(add = 0), c.end], # fim da história
          [c.beg, c.mau, c.ID('Desenhista 1'), c.ID('Desenhista 2'), c.ID('Desenhista 3'), c.ID('Desenhista 4'), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mau, c.ID('Desenhista 1'), c.ID('Desenhista 2'), c.ID('Desenhista 3'), c.ID('Desenhista 4'), c.tin, c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()], # fim da história
          [c.naj, c.jot, c.anim(), c.end], # fim da história
          [], # [c.dud, c.cas, 'Anjinho', c.franj, c.mon], # passatempos
          [], # [c.mon, c.mag, c.cas, c.ceb, c.bid, c.xav, c.pen], # correio
          [], # [c.mon, c.mag, c.chi, c.nim, c.cas], # tem três meninas que não conheço (correio)
          [c.beg, c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra],
          [c.lob, c.pen, c.fra, c.fig()],
          [c.lob, c.pen, c.fra, c.fig(add = 0)],
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
          [c.beg, c.zcav, c.anim(), c.end], # fim da história
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
