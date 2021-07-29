from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 6'

pages6 = [[c.beg, c.san, c.ceb, c.cas, c.mon, c.end], # capa
          [],
          [c.san, c.ceb, c.cas, c.mon], # introdução
          [c.beg, c.child(), c.child(), c.mceb, c.ceb, c.cas, 'Tartaruga', 'Lebre', c.shade(), c.shade()], # figurantes na sombra
          [c.ceb, c.cas, c.fig(), c.child(), c.child(), c.child(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.san],
          [c.san, c.ceb, c.cas, c.mon, c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()],
          [c.san, c.ceb, c.cas, c.mon],
          [c.san, c.ceb, c.cas, c.mon],
          [c.mon, c.ceb, c.cas, 'Cérebro do Cebolinha'],
          [c.ceb, c.cas],
          [c.ceb, c.cas, c.san],
          [c.ceb, c.cas, c.san],
          [c.ceb, c.cas, c.san],
          [c.ceb, c.cas, c.san, c.child(), c.child()],
          [c.ceb, c.cas, c.san, c.child(), c.att(), c.mon],
          [c.ceb, c.cas, c.san],
          [c.ceb, c.cas, c.child()],
          [c.ceb, c.cas],
          [c.ceb, c.cas],
          [c.ceb, c.cas, 'Moça achados e perdidos'],
          [c.ceb, c.cas, 'Moça achados e perdidos', c.mon],
          [c.ceb, c.cas, 'Moça achados e perdidos', c.mon],
          [c.ceb, c.cas, 'Cérebro do Cebolinha', c.mon],
          ['Moça achados e perdidos', c.ceb, c.cas, c.mon, c.mceb, c.mot(), c.child(), c.shade(), c.end], # fim da história
          [c.beg, c.san, c.ceb, c.mon, c.mag],
          [c.mag, c.mon, c.san],
          [c.mag, c.mon, c.san, c.cas, c.end], # fim da história
          [c.beg, c.mon],
          [c.mon, c.san, c.ceb, c.end], # fim da história
          [],
          [],
          [c.beg, c.mon, c.san, c.ceb, c.cas, c.end], # fim da história
          [], # [c.ceb, c.mag, c.cas, c.mon, c.san], # passatempos
          [], # [c.ceb, c.mag, c.cas, c.mon, c.san, c.bid], # correio
          [], # [c.ceb, 'Bolinha amarela estranha'], # correio
          [c.beg, c.ceb, c.mon, c.mceb, c.san],
          [c.ceb, c.mon, c.mceb, c.san, c.end], # fim da história
          [c.beg, c.pen, 'Cupido', c.fra, 'Moça'],
          [c.pen, c.zvam, c.lob, 'Morcego', 'Cachorro', 'Cupido'], # morcego é quem se apaixonou pelo zé vampir e cachorro pelo lobi
          [c.fra, 'Moça', c.lob, 'Cachorro', c.zvam, 'Morcego', c.pen, 'Cupido', c.alm, c.end], # fim da história
          [],
          [c.beg, c.chi, c.nho, c.end], # fim da história
          [c.beg, c.rol, 'Verinha'],
          [c.rol, 'Verinha'],
          [c.rol, 'Verinha', c.fig(), c.end], # fim da história
          [c.beg, c.luc],
          [c.luc, c.ceb, c.cas],
          [c.luc, c.ceb, c.cas, c.mon, c.san],
          [c.luc, c.mon, c.san, c.mag, c.den],
          [c.luc, c.mon, c.ceb, c.cas, c.franj],
          [c.luc],
          [c.luc, c.min, c.bid, c.mag, c.mon, c.san, c.xav, c.cas, c.pxav, 'Banda', c.child(), 'Elefante', 'Sequestradores'],
          [c.luc],
          [c.luc, c.ceb, c.cas, 'Médico', c.end], # fim da história
          [],
          [c.beg, c.chi, c.ros, c.prof],
          [c.chi, c.pad, c.mchi, 'Dentista', c.end], # fim da história
          [c.beg, c.mon, c.ceb],
          [c.mon, c.ceb, c.cas],
          [c.mon, c.ceb, c.cas],
          [c.mon, c.ceb, 'Fabinho'], # fabinho só em caricatura num balão de fala
          [c.mon, c.ceb, 'Fabinho'], # e agora ao vivo
          [c.mon, c.ceb, c.child(), c.mot(), c.fig()],
          [c.mon, c.ceb, c.mar],
          [c.mon, c.ceb, c.mar, c.end], # fim da história
          [c.beg, c.pen, c.zcav, c.end]] # tirinha final
