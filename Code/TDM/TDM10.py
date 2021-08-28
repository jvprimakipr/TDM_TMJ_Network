from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm10'

pages10 = [[c.beg, c.cas, c.ceb, c.end],
	   [],
	   [c.ceb, c.cas],
	   [c.beg, c.cas, c.ceb, c.child(), c.child(), c.child()],
	   [c.ceb, c.cas, c.pcas],
	   [c.ceb, c.cas, c.pcas],
	   [c.ceb, c.cas, c.att(), c.child()] + c.shades(11),
	   [c.ceb, c.cas, c.child(), c.child(), c.fig(), c.fig()] + c.shades(4),
	   [c.ceb, c.cas],
	   [c.ceb, c.cas],
	   [c.san, c.ceb, c.cas, c.mon],
	   [c.san, c.ceb, c.cas, c.mon],
	   [c.san, c.ceb, c.cas, c.mon, c.child()],
	   [c.san, c.ceb, c.cas, c.mon],
	   [c.san, c.cas, c.ceb, c.mon],
	   [c.san, c.cas, c.ceb, c.mon],
	   [c.san, c.cas, c.ceb, c.mon, c.att(), c.child()],
	   [c.san, c.cas, c.ceb, c.mon],
	   [c.mon, c.cas, c.ceb, c.child(), c.child(), c.child()] + c.shades(9),
	   [c.san, c.cas, c.ceb, c.mon, c.shade()],
	   [c.san, c.cas, c.ceb, c.mon],
	   [c.san, c.cas, c.ceb, c.mon, c.shade(), c.shade()],
	   [c.san, c.cas, c.ceb, c.mon] + c.shades(6) + [c.end], # end no final só por padrão meu mesmo, mas poderia ser no meio ;-)
	   [c.beg, c.chi, c.child(), c.anim(), c.gis, c.mim, c.tor, c.anim(), 'Onça', c.anim(), c.anim(), c.anim(), c.anim(), c.end],
	   [],
	   [c.beg, c.bid, c.zesq],
	   [c.bid, c.zesq],
	   [c.zesq, c.child()],
	   [c.zesq, c.anim()],
	   [c.zesq, c.anim(add = 0), c.bid],
	   [c.zesq, c.bid, c.duq, c.end], #PRIMAKI, help
	   [c.beg, c.cra, c.end],
	   [],
	   [], # [c.anj, c.mceb, c.marceb, c.mon, c.cas], # correio
	   [], # [c.ceb, c.mag, c.xav, 'Muleke estranho'], # correio
	   [], # [c.ast, c.mon, c.ceb], # passatempos
	   [],
	   [c.beg, c.zvam, c.cb + 'Mulher 1'],
	   [c.pen, c.zvam, c.cb + 'Mulher 1'],
	   [c.pen, c.zvam],
	   [c.pen, c.zvam],
	   [c.pen, c.zvam],
	   [c.pen, c.zvam, c.mum],
	   [c.pen, c.zvam, c.mum, c.fra],
	   [c.fra, c.pen, c.zvam, c.lob],
	   [c.pen, c.zvam],
	   [c.pen, c.zcav, c.zvam, c.cb + 'Mulher 2', c.end],
	   [c.beg, c.mar, c.jer, 'Tia do Jeremias', c.cb + 'Mulher 3'],
	   [c.mar, 'Tia do Jeremias', c.mag, c.tit, c.xav],
	   [c.mag, c.tit, c.xav, c.ceb, ], #PRIMAKI, help
	   [c.ceb, c.hum, c.san],
	   [c.mon, c.san, c.ceb, 'Tia do Jeremias', c.tit, c.mar, c.end],
	   [],
	   [c.beg, c.cb + 'Homem 1', c.child()],
	   [c.cb + 'Mulher 4', c.cb + 'Homem 2', c.fig(), c.child(), c.child(), c.anim(), c.fig(), c.fig(), c.fat(), c.child(), c.mor, c.end],
	   [c.beg, c.ceb, c.cas, c.pceb],
	   [c.ceb, c.cas, c.pceb],
	   [c.ceb, c.cas],
	   [c.ceb, c.cas, 'Homem de Chumbo', 'Zing Mascarado', c.mceb],
	   [c.ceb, c.cas, c.mceb],
	   [c.ceb, c.cas, 'Homem de Chumbo', 'Zing Mascarado', c.mceb],
	   [c.ceb, c.cas, 'Homem de Chumbo', 'Zing Mascarado'],
	   [c.ceb, c.cas, 'Homem de Chumbo', 'Zing Mascarado'],
	   [c.ceb, c.cas, 'Homem de Chumbo', 'Zing Mascarado'],
	   [c.ceb, c.cas, c.pceb, c.mceb, c.end],
	   [c.beg, c.ceb, c.xav, c.cas, c.end]]
