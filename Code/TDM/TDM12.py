from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm12'
c.cb = c.comic_book + ' '

pages12 = [[c.beg, c.cas, c.ceb, c.marcas, c.mon, c.mag, c.end],
           [],
           [c.beg, c.marcas, c.mag, c.den, c.mon],
           [c.mon, c.den, c.marcas],
           [c.mon, c.marcas, c.den, c.mag],
           [c.mon, c.marcas, c.den, c.mag, c.ceb, c.cas] + c.shades(10),
           [c.ceb, c.cas],
           [c.ceb, c.cas, c.xav] + c.kids(7),
           [c.ceb, c.xav, c.mon, c.den, c.marcas, c.mag, c.fabbp],
           [c.mon, c.den, c.marcas, c.mag, c.fabbp, c.ceb, c.cas, c.xav, c.child(), c.shade(), c.shade()],
           [c.mon, c.den, c.marcas, c.mag, c.fabbp, c.ceb, c.cas],
           [c.mon, c.den, c.marcas, c.mag, c.ric, c.ceb, c.cas, c.xav],
           [c.mon, c.den, c.marcas, c.mag, c.ric],
           [c.mon, c.den, c.marcas, c.mag, c.ber, c.ceb, c.cas, c.xav, c.child()] + c.shades(11),
           [c.mon, c.den, c.marcas, c.ber, c.luc],
           [c.mon, c.den, c.marcas, c.mag, c.luc, c.ceb, c.cas, c.xav],
           [c.mon, c.den, c.marcas, c.mag, c.ceb, c.cas, c.xav],
           [c.mon, c.den, c.marcas, c.mag, c.ceb, c.cas, c.xav, c.quin, c.child()],
           [c.mon, c.den, c.marcas, c.ceb, c.cas, c.xav, c.ber, c.fabbp, c.ric, c.luc, c.san, c.end],
           [c.beg, c.bol, c.thu],
           [c.thu, c.bol, c.pit, c.end],
           [],
           [],
           [c.beg, c.mmon, c.mon, c.san, c.ceb, c.mceb, c.cas, c.mcas, c.mag, c.mmag],
           [c.mag, c.mmag, c.end],
           [c.beg, c.marceb, c.dud], #PRIMAKI ver essa história, todo mundo pensa no seu futuro
           [c.marceb, c.dud, c.cas, c.ceb, c.tit, c.man, c.jer],
           [c.ceb, c.cas, c.zlui, c.tit, c.man, c.jer, c.pceb, c.mceb, c.fig(), c.shade(), c.shade()], #PRIMAKI, quem é a moça?
           [c.zlui, c.pceb, c.marceb, c.end], # e a moça?
           [c.beg, c.san, c.mon, c.ceb],
           [c.san, c.mon, c.ceb, c.end],
           [c.beg, c.cas, c.anim(), c.anim(), c.anim(), c.end],
           [], # [c.tin, c.zec, c.rol] # passatempos
           [], # [c.bid, c.ani, c.tit, c.mon] # correio
           [], # [c.dor, c.lou] # correio (ver quem é o cara estranho ali)
           [c.beg, c.chi, c.zlel, c.anim()], # duende narrando entra?
           [c.chi, c.zlel, c.anim(add = 0), c.cb + 'Bruxo'],
           [c.chi, c.zlel, c.anim(add = 0), c.cb + 'Bruxo'],
           [c.chi, c.zlel, c.anim(add = 0)], # abóboras com pernas contam?
           [c.chi, c.zlel, c.anim(add = 0), 'Duende', c.end], # idem ^^
           [],
           [c.beg, c.bid, c.mag],
           [c.mag, c.bid, c.min],
           [c.mag, c.min, c.chov, c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim()],
           [c.mag, c.bid, c.min, c.chov, c.fig(), c.end], # esse padeiro tem nome?
           [c.beg, c.pen, c.zvam],
           [c.pen, c.zvam],
           [c.pen, c.zvam],
           [c.pen, c.zvam],
           [c.pen, c.zvam],
           [c.pen, c.zvam],
           [c.pen, c.zvam],
           [c.pen, c.zvam, c.alm],
           [],
           [c.beg, c.ceb, c.cas, c.end],
           [c.beg, c.ceb, c.mon, c.floq, c.san],
           [c.ceb, c.san, c.mon, c.anim(), c.end],
           [c.beg, c.mon, c.san],
           [c.mon],
           [c.mon, c.moca],
           [c.mon, c.moca],
           [c.mon, c.moca],
           [c.mon, c.moca],
           [c.mon, c.moca],
           [c.mon, c.moca, c.fabbp, c.den, c.child(), c.child(), c.child(), c.shade()],
           [c.beg, c.ceb, c.mon, c.doc, c.end],
           [],
           []]
