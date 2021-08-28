from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm16'
c.cb = c.comic_book + ' '

pages16 = [[c.beg, c.chi, c.child(), 'Espírito do Milharal', c.end],
		   [],
		   [c.chi, 'Espírito do Milharal'],
		   [c.beg, c.chi, c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim()],
		   [c.chi, c.nho],
		   [c.chi, c.nho],
		   [c.chi, 'Espírito do Milharal'], # Espírito do Milharal só em um balão de fala
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal', c.anim(), c.anim()] + c.shades(3),
		   [c.chi, 'Espírito do Milharal'], # ambos só em balão de fala
		   [c.chi, 'Espírito do Milharal', c.fat(), c.mot(), c.mot(), c.att()] + c.kids(3) + c.shades(14),
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal', c.att()] + c.kids(4),
		   [c.chi, 'Espírito do Milharal', c.child(), c.att(add = 0)],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, 'Espírito do Milharal', c.fig()],
		   [c.chi, 'Espírito do Milharal', c.fig()], # figurante só em balão de fala (motorista do ônibus falando da próxima parada)
		   [c.chi, 'Espírito do Milharal'],
		   [c.chi, c.nho],
		   [c.chi, c.nho, c.end],
		   [],
		   [c.beg, c.bid],
		   [c.bid, c.duq, 'Zé Gordão', c.anim()], # conferir os dois últimos
		   [c.bid, c.duq, 'Zé Gordão', c.anim(add = 0), c.end],
		   [], # [c.tin, c.pip, c.rol, c.zec] # passatempo
		   [], # [c.ceb, c.mon, c.anj] # correio
		   [], # [c.tit, c.mon, c.ceb, c.den] # correio (conferir denise)
		   [],
		   [c.beg, c.dor, c.mdor],
		   [c.dor, c.mdor],
		   [c.dor, c.mdor, c.mag, c.mmag, c.end],
		   [c.beg, c.cas],
		   [c.cas, c.end],
		   [c.beg, c.mag, c.min], # mingau só em balão de fala
		   [c.mag, c.min, c.end],
		   [c.beg, c.pap, c.caf, c.fig()],
		   [c.fig(add = 0), c.jur, c.cb + 'Indiazinha 1', c.cb + 'Índio', c.cb + 'Índia', c.fig(), c.cb + 'Indiazinha 2', c.cb + 'Indiazinha 3', c.end],
		   [],
		   [c.beg, c.cas, c.ceb, c.doc, c.end],
		   [c.beg, c.fra, c.fig(), c.fig(), c.anim()],
		   [c.fra, c.fig(add = 0), c.fig(add = -1), c.anim()],
		   [c.fra, c.fig(), c.pen],
		   [c.fra, c.fig(add = 0), c.pen],
		   [c.fra, c.fig(), c.zvam],
		   [c.fra, c.fig(add = 0), c.zvam, c.lob, c.fig()],
		   [c.fra, c.fig(add = 0), c.lob],
		   [c.fra, c.fig(), c.fig(), c.cra, c.zcav, c.mum],
		   [c.fra, c.fig(add = 0), c.fig(add = -1), c.fig(), c.fig()],
		   [c.fra] + c.figs(5) + [c.end],
		   [],
		   [c.beg, c.chi, c.nho],
		   [c.chi, c.nho],
		   [c.chi, c.nho],
		   [c.chi, c.nho],
		   [c.chi, c.nho, c.anim()],
		   [c.chi, c.nho, c.fig(), c.fig()],
		   [c.chi, c.nho, c.fig(add = 0), c.fig(add = -1), c.end],
		   [c.beg, c.cra, c.cb + 'Fantasminha', c.end]]
