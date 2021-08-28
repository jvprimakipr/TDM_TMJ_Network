from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm17'
c.cb = c.comic_book + ' '

pages17 = [[c.beg, c.ceb, c.san, c.cas] + c.figs(17) + [c.end], # figurantes são de tudo (mães, pais, crianças, atendentes, mas joguei só figurante mesmo)
		   [],
		   [c.cas, c.ceb],
		   [c.beg, c.cas, c.ceb],
		   [c.cas, c.ceb],
		   [c.cas, c.ceb],
		   [c.cas, c.ceb],
		   [c.cas, c.ceb],
		   [c.cas, c.ceb],
		   [c.cas, c.ceb],
		   [c.cas, c.ceb, c.san],
		   [c.cas, c.ceb],
		   [c.cas, c.ceb] + c.kids(3),
		   [c.cas, c.ceb],
		   [c.cas, c.ceb, c.child()],
		   [c.cas, c.ceb, c.child(add = 0)],
		   [c.cas, c.ceb, c.san, c.mon, c.mag],
		   [c.cas, c.ceb, c.san, c.mon, c.mag],
		   [c.cas, c.ceb, c.san, c.mon, c.mag, c.mot(), c.att(), c.child(), c.child()] + c.shades(14),
		   [c.ceb, c.san, c.mon, c.att()] + c.kids(7),
		   [c.cas, c.ceb, c.san, c.mon, c.mag],
		   [c.cas, c.ceb, c.child(), c.shade(), c.shade()],
		   [c.cas, c.ceb],
		   [c.ceb, c.fat(), c.fat(), c.cb + 'Gnomo do Papai Noel 1', c.cb + 'Gnomo do Papai Noel 2', c.cb + 'Gnomo do Papai Noel 3'] + c.kids(7) + c.shades(14),
		   [c.ceb, c.san, c.fat(), c.child()] + c.shades(4),
		   [c.ceb, c.san, c.mon],
		   [c.ceb, c.mon, 'Papai Noel', c.cb + 'Gnomo do Papai Noel 4', c.fig()] + c.shades(12) + [c.end],
		   [c.beg, c.nicdem],
		   [c.nicdem, c.end],
		   [c.beg, c.mon, c.san, c.ceb],
		   [c.mon, c.san, c.ceb, c.end],
		   [],
		   [], # [c.dor, c.rad] # passatempo
		   [], # [c.ceb, c.blo, c.san] # correio
		   [], # [c.mar, c.anj, c.mag] # correio
		   [],
		   [c.beg, c.zlel, c.marcaf, c.anim()],
		   [c.zlel, c.marcaf, c.anim(add = 0)],
		   [c.zlel, c.marcaf, c.anim(), c.anim()],
		   [c.zlel, c.marcaf, c.anim(add = -1)],
		   [c.zlel, c.marcaf],
		   [c.zlel, c.marcaf, c.anim(add = -1), c.anim(add = 0)],
		   [c.zlel, c.marcaf, c.end],
		   [],
		   [c.beg, c.fig(), c.fig(), c.end],
		   [c.beg, c.mon, c.san, c.cas, c.marcas, c.tit, c.ani],
		   [c.mon, c.san, c.mag, c.quin, c.ceb, c.end],
		   [],
		   [c.beg, c.cas, c.ceb, c.mag, c.mon, c.bid, 'Homem de Chumbo', 'Zing Mascarado', 'Alberto Aíston'],
		   [c.mag, 'Sônico'],
		   [c.mag, c.ceb, c.cas, c.mon, c.san, 'Sônico'],
		   [c.mag, c.ceb, c.cas, c.mon, 'Sônico'],
		   [c.ceb, c.cas, c.mon, 'Sônico', c.franj, c.bid],
		   [c.ceb, c.cas, c.mon, c.mag, c.franj, c.san],
		   [c.ceb, c.cas, c.mon, c.franj, c.san],
		   [c.mag, c.ceb, c.cas, c.mon, c.franj, 'Sônico'],
		   [c.mag, c.ceb, c.cas, c.mon, c.pceb],
		   [c.pceb, c.mceb],
		   [c.mag, c.ceb, c.cas, c.mon, c.franj, 'Sônico', 'Alberto Aíston'] + c.figs(4) + c.shades(2),
		   [c.mag, c.ceb, c.cas, c.mon, 'Sônico', 'Alberto Aíston', c.cb + 'Personagem de jogo'],
		   [c.mag, c.ceb, c.cas, c.mon, 'Sônico', 'Alberto Aíston', c.cb + 'Personagem de jogo', 'Princesa Pesseguinho'],
		   [c.mag, c.ceb, c.cas, c.mon, 'Sônico', 'Alberto Aíston', 'Zelda', 'Pacman'],
		   [c.ceb, c.blo, c.cas, c.franj, 'Sônico', 'Mario Vermelho', c.mon], # franjinha só falando pelo relógio comunicador
		   ['Sônico', c.mon, c.cas, c.blo, 'Alberto Aíston', 'Homem de Chumbo', 'Zing Mascarado', c.mag, c.ceb, c.franj, c.cb + 'Personagem de jogo 2'], # rt para o franjinha (o mesmo para o último personagem)
		   [c.cb + 'Personagem de jogo 2', c.cb + 'Personagem de jogo 3', c.mag, c.mon, c.ceb, c.franj, c.blo, 'Sônico', c.cas, 'Alberto Aíston', c.cb + 'Personagem de jogo 4', c.cb + 'Personagem de jogo 5', 'Pacman', c.end],
		   [c.beg, c.doc, c.end],
		   [],
		   [],
		   []]
