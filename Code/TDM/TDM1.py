from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 1'

pages1 = [[c.viv, c.mon, c.ceb, c.mag], # capa
          [],
          [c.viv, c.bor, c.mon, c.ceb, c.mag, c.san], # introdução
          [c.viv, c.bor],
          [c.viv, c.bor, c.mon, c.mag, c.ceb, c.cas],
          [c.viv, c.bor],
          [c.viv, c.bor],
          [c.viv, c.bor, c.att(), c.att()],
          [c.viv, c.bor, c.att(n = 1)],
          [c.viv, c.bor, c.att(n = 1)],
          [c.viv, c.bor, c.ceb, c.cas],
          [c.viv, c.bor, c.mon, c.ceb, c.cas],
          [c.viv, c.bor, c.mon, c.ceb, c.cas],
          [c.viv, c.mon, c.ceb, c.cas],
          [c.viv, c.mon, c.ceb, c.cas],
          [c.viv, c.bor, c.mon, c.ceb, c.cas],
          [c.viv, c.bor, c.mag, c.child()],
          [c.viv, c.bor, c.mag],
          [c.viv, c.bor, c.mag, c.fig(), c.att()],
          [c.viv, c.mag, c.att()],
          [c.viv, c.mon, c.mag, c.ceb, c.cas, c.att(n = 4)],
          [c.viv, c.mon, c.mag, c.ceb, c.cas],
          [c.viv, c.mon, c.mag, c.ceb, c.cas],
          [c.viv, c.mon, c.mag, c.ceb, c.cas, 'Dinossauro 1 - gibi 1', 'Dinossauro 2 - gibi 1', 'Dinossauro 3 - gibi 1'],
          [c.viv, c.mag, 'Dinossauro 1 - gibi 1', 'Dinossauro 2 - gibi 1', 'Dinossauro 3 - gibi 1', 'Dinossauro 4 - gibi 1'],
          [c.viv, c.bor, c.mag],
          [c.viv, c.bor, c.mon, c.mag, c.ceb, c.cas], # fim da história
          [],
          [],
          [c.pit],
          [c.pit],
          [c.pit, 'Dinossauro verde'],
          [c.pit, 'Dinossauro verde'], # fim da história
          [],
          [],
          [],
          [],
          [c.pen],
          [c.pen, 'Gato laranja'], # fim da história
          [c.ceb, c.floq],
          [c.ceb, c.floq], # fim da história
          [c.dud, c.mdud],
          [c.dud, 'Lactos Kid'],
          [c.dud, 'Lactos Kid', 'Milhus', 'Ervilhus'],
          [c.dud, 'Lactos Kid', 'Milhus', 'Ervilhus', 'Macarrônios', 'Povo Feijônico', 'Monstro Q.I. Jo'],
          [c.dud, c.mdud, 'Lactos Kid', 'Milhus', 'Ervilhus', 'Povo Feijônico'], # fim da história
          [],
          [c.bid, c.franj, c.ceb],
          [c.bid, c.ceb, c.mon, c.cas], # fim da história
          [c.ast, 'Monstro Verde Grande', 'Monstro Rosa'],
          [c.ast, 'Monstro Rosa', 'Monstro Verde Pequeno'], # fim da história
          [c.zlel, c.fig(), c.fig(), c.att(), 'Galinha do Zé Lelé', 'Pintinho'],
          [c.zlel, 'Galinha do Zé Lelé', c.att(n = 5), c.att(), c.child(), c.child(), c.child(), c.child(), c.child(),
           c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child()], # fim da história
          [],
          [c.zlel, 'Galinha do Zé Lelé', c.mlel, c.child(), c.child(), c.child(), c.child()],
          [c.lob, 'Cachorro 1', 'Cachorro 2', 'Peixe', 'Pássaro', 'Menino de cabelo laranja e camisa verde'],
          [c.lob, 'Cachorro 1', 'Cachorro 2', c.child(), c.fig()], # fim da história
          [c.mon, c.franj, c.bid], # bidu e  franjinha em pensamento
          [c.mon, c.mag, c.min, c.ceb, c.floq], # só mônica e cebolinha, o resto é pensamento / fim da história
          [c.tin, c.pip],
          [c.tin, c.pip, c.ser],
          [c.tin, c.pip, c.ser],
          [c.tin, c.pip],
          [c.tin, c.pip, c.ser],
          [c.tin, c.pip, c.ser], # fim da história
          [c.zvam, c.mum, c.pen, c.cra]] # última página (tirinha)
