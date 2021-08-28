from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm01'
c.cb = c.comic_book + ' '

pages1 = [[c.beg, c.viv, c.mon, c.ceb, c.mag, c.end], # capa
          [],
          [c.viv, c.bor, c.mon, c.ceb, c.mag, c.san], # introdução
          [c.beg, c.viv, c.bor],
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
          [c.viv, c.mon, c.mag, c.ceb, c.cas, c.anim(), c.anim(), c.anim()],
          [c.viv, c.mag, c.anim(add = -2), c.anim(add = -1), c.anim(add = 0), c.anim()],
          [c.viv, c.bor, c.mag],
          [c.viv, c.bor, c.mon, c.mag, c.ceb, c.cas, c.end],
          [],
          [],
          [c.beg, c.pit],
          [c.pit],
          [c.pit, c.dino()],
          [c.pit, c.dino(add = 0), c.end],
          [],
          [],
          [],
          [],
          [c.beg, c.pen],
          [c.pen, c.anim(), c.end],
          [c.beg, c.ceb, c.floq],
          [c.ceb, c.floq, c.end],
          [c.beg, c.dud, c.mdud],
          [c.dud, 'Lactos Kid'],
          [c.dud, 'Lactos Kid', 'Milhus', 'Ervilhus'],
          [c.dud, 'Lactos Kid', 'Milhus', 'Ervilhus', 'Macarrônios', 'Povo Feijônico', 'Monstro Q.I. Jo'],
          [c.dud, c.mdud, 'Lactos Kid', 'Milhus', 'Ervilhus', 'Povo Feijônico', c.end],
          [],
          [c.beg, c.bid, c.franj, c.ceb],
          [c.bid, c.ceb, c.mon, c.cas, c.end],
          [c.beg, c.ast, c.mons(), c.mons()],
          [c.ast, c.mons(add = 0), c.mons(), c.end],
          [c.beg, c.zlel, c.fig(), c.fig(), c.att(), c.gis, c.anim()],
          [c.zlel, c.gis, c.att(n = 5), c.att(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.end],
          [],
          [c.beg, c.zlel, c.gis, c.mlel, c.child(), c.child(), c.child(), c.child()],
          [c.lob, c.anim(), c.anim(), c.anim(), c.anim(), c.cb + 'Menino de cabelo laranja e camisa verde'], # PRIMAKI
          [c.lob, c.anim(add = -3), c.anim(add = -2), c.child(), c.fig(), c.end],
          [c.beg, c.mon, c.franj, c.bid], # bidu e  franjinha em pensamento
          [c.mon, c.mag, c.min, c.ceb, c.floq, c.end], # só mônica e cebolinha, o resto é pensamento
          [c.beg, c.tin, c.pip],
          [c.tin, c.pip, c.ser],
          [c.tin, c.pip, c.ser],
          [c.tin, c.pip],
          [c.tin, c.pip, c.ser],
          [c.tin, c.pip, c.ser, c.end],
          [c.beg, c.zvam, c.mum, c.pen, c.cra, c.end]] # última página (tirinha)
