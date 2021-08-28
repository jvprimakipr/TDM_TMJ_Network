from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm07'

pages7 = [[c.beg, c.mon, c.mar, c.ceb, c.cas, c.xav, c.nim, c.doc, c.hum, c.jer, c.end],
          [],
          [c.den, c.mon, c.carfru, c.den, c.mag],
          [c.beg, c.mar, c.mon, c.mag],
          [c.mar, c.mon, c.mag],
          [c.mon, c.mag, c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mar, c.mon, c.mag, c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mar, c.mon],
          [c.mon, c.mar, c.ceb, c.cas, c.child(), c.child(), c.child(), c.shade(), c.shade(), c.shade()],
          [c.cas, c.ceb, c.mon, c.mar],
          [c.cas, c.ceb, c.mar, c.mag, c.mon, c.nim, c.xav, c.hum],
          [c.cas, c.ceb, c.mar, c.mag, c.mon, c.nim, c.xav, c.hum, c.den, c.carfru],
          [c.cas, c.ceb, c.mar, c.mag, c.mon, c.nim, c.xav, c.hum, c.den, c.carfru],
          [c.cas, c.ceb, c.mag, c.mon, c.nim, c.xav, c.hum, c.carfru],
          [c.cas, c.ceb, c.mar, c.mag, c.mon, c.nim, c.xav, c.hum, c.den, c.carfru],
          [c.ceb, c.mar, c.mag, c.mon, c.nim, c.den, c.carfru, c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.shade(), c.shade()],
          [c.mon, c.mag, c.den, c.carfru, c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.mon, c.mag, c.den, c.carfru, c.mar, c.mau, c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mon, c.mag, c.den, c.carfru, c.mar, c.mau, c.ali, c.child(add = -1), c.child(add = -2), c.child(add = -3), c.child(add = -4), c.child(add = -5), c.child(add = -6), c.child(add = -7), c.child(add = -8), c.child(add = -9), c.child(add = -10), c.child(add = -11), c.child(add = -12), c.shade(add = -1), c.shade(add = -2), c.shade(add = -3), c.shade(add = -4), c.shade(add = -5), c.shade(add = -6)], # coloquei repetidos por que daria muita criança num só gibi / fim da história
          [c.cas, c.ceb, c.end], # fim da história
          [],
          [c.beg, c.mag, c.ceb, c.mon, c.san, c.mmag],
          [c.mon, c.san, c.ceb, c.cas, c.mcas, c.zlui, c.end], # fim da história
          [c.beg, c.cas, c.mon, c.ceb],
          [c.cas, c.mag, c.mau, c.ali, c.end], # fim da história
          [c.beg, c.paj],
          [c.paj, c.cac, c.cb + 'Índia', c.cb + 'Índio'],
          [c.paj, c.cac, c.cb + 'Índia', c.cb + 'Índio', c.pap, c.end], # fim da história
          [c.beg, c.cas],
          [c.mon, c.mag, c.ceb],
          [c.dud, c.xav, c.spa, c.anj, c.cb + 'Anjo 1', c.cb + 'Anjo 2', c.cb + 'Anjo 3', c.end], # fim da história
          [],
          [], # [c.jot, c.mon, c.ceb, c.cas, c.mag], # passatempo
          [], # [c.mon, c.mag, c.ceb, c.cas, c.bid, c.gen], # correio
          [], # [c.mon, c.quin, c.nim, c.cas], # correio
          [c.beg, c.fig(), c.mon, c.mag, c.fig(), c.shade(), c.shade(), c.shade(), c.fig(), c.fig()],
          [c.fig(), c.mon, c.mag, c.shade(add = -1), c.shade(add = -2), c.shade(add = -3), c.shade(), c.shade(), c.shade(), c.shade(), c.fig()], # fim da história
          [c.fig(), c.fig(), c.fig()],
          [c.fig(add = 0), c.fig(), c.pen, 'Fantasma do Sultão', c.end], # fim da história
          [],
          [],
          [c.beg, c.mar],
          [c.mar, c.anim()],
          [c.mar, c.anim()],
          [c.mar, c.luc, c.mon, c.den, c.mag, c.end], # fim da história
          [c.beg, c.ceb, c.mag, c.mon],
          [c.ceb, c.mon, c.mag, c.cb + 'Alienígena 1', c.cb + 'Alienígena 2', c.cb + 'Alienígena 3', c.cb + 'Alienígena 4', c.cb + 'Alienígena 5', c.cb + 'Alienígena 6'], # fim da história
          [c.ast],
          [c.ast, c.mons()],
          [c.ast, c.mons(add = 0)],
          [c.ast, c.mons(add = 0), 'Computador do Astronauta', c.mons(), c.mons(), c.mons()],
          [c.ast, c.mons(add = -2), c.mons(add = -1), c.mons(add = 0)],
          [c.ast, c.mons(add = -2), c.mons(add = -1), c.mons(add = 0), c.mons(), c.fig(), c.fig()],
          [c.ast, c.mons(add = -2), c.mons(add = -1), c.mons(add = -3)],
          [c.ast, c.mons(add = -2), c.mons(add = -1), c.mons(add = -3)],
          [c.ast, c.mons(add = -2), c.mons(add = -1), c.mons(add = -3)],
          [c.ast, c.mons(add = -2), c.mons(add = -1), c.mons(add = -3), c.mast, c.end], # fim da história
          [c.beg, c.mon, c.mmon, c.ceb, c.mceb, c.mag, c.mmag, c.cas, c.mcas, c.end], # fim da história
          [c.beg, c.ceb],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb],
          [c.mau, c.mar, c.end], # fim da história
          [c.beg, c.ceb, c.lou, c.end]] # tirinha do final
