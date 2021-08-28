from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm15'
c.cb = c.comic_book + ' '

pages15 = [[c.beg, c.anj, c.cas, c.ceb, c.mon, c.mag, c.san, c.end],
           [],
           [c.anj, c.cas, c.ceb, c.mon, c.mag, c.cb + 'Anjinho Substituto'],
           [c.beg, c.cas, c.ceb, c.mon, c.mag, c.mmag, c.fat(), c.child()] + c.shades(4),
           [c.cas, c.ceb, c.mon, c.mag],
           [c.cas, c.ceb, c.mon, c.mag, c.mot(), c.mot(), c.att()] + c.kids(4) + c.shades(4),
           [c.cas, c.ceb, c.mon, c.mag],
           [c.cas, c.ceb, c.mon, c.mag, c.anj],
           [c.cas, c.ceb, c.mon, c.mag, c.anj],
           [c.mon, c.anj],
           [c.mon, c.anj, c.fat()] + c.kids(4),
           [c.mon, c.anj],
           [c.mon, c.anj, c.child(), c.child()],
           [c.cas, c.ceb, c.mon, c.mag, c.anj],
           [c.cas, c.ceb, c.mon, c.mag, c.anj],
           [c.cas, c.ceb, c.mon, c.mag, c.anj],
           [c.anj] + [f'{c.comic_book} Anjo {i + 1}' for i in range(18)] + [c.end],
           [c.beg, c.ast, c.mons()],
           [c.ast, c.mons(add = 0), c.end],
           [],
           [c.beg, c.pit, c.dino()],
           [c.pit, c.dino(n = 1), c.cave(n = 1)],
           [c.pit, c.dino(n = 1), c.cave(n = 1), c.thu, c.bol, c.var, c.cave(n = 8)],
           [c.pit, c.thu, c.bol, c.var, c.cave(n = 8)],
           [c.pit, c.dino(n = 1), c.dino(n = 2), c.bol, c.var, c.cave(n = 8)],
           [c.pit, c.dino(n = 1), c.dino(n = 2), c.dino(n = 3), c.bol, c.var, c.cave(n = 8), c.cave(n = 1), c.cave(n = 7)],
           [c.pit, c.dino(n = 1), c.bol, c.var, c.cave(n = 8), c.cave(n = 1), c.cave(n = 7), c.cave(n = 2)] + c.shades(2),
           [c.pit, c.thu, c.bol, c.var, c.cave(n = 8), c.cave(n = 7), c.cave(n = 2)],
           [c.pit, c.thu, c.bol, c.var, c.cave(n = 8), c.cave(n = 7), c.cave(n = 2), c.cave(n = 3), c.cave(n = 4), c.cave(n = 5)],
           [c.pit, c.thu, c.bol, c.cave(n = 8), c.cave(n = 1), c.cave(n = 4), c.cave(n = 5), c.dino(n = 1)],
           [c.pit, c.thu, c.bol, c.var, c.cave(n = 1), c.cave(n = 4), c.cave(n = 5), c.cave(n = 6), c.dino(n = 1)],
           [c.pit, c.var, c.bol, c.thu, c.end],
           [], # [c.bid] # passatempo
           [], # [c.mon, c.ceb, c.mag, c.min] # correio
           [], # [c.anj, c.cas, c.mag, c.hor] # correio
           [],
           [c.beg, c.mon, c.cas],
           [c.mon, c.san],
           [c.mon],
           [c.mon],
           [c.mon, c.san, c.mmon, c.pmon, c.end],
           [c.beg, c.ceb, c.pceb, c.end],
           [c.beg, c.nicdem, c.child()],
           [c.nicdem, c.child(add = -1), c.child()],
           [c.nicdem, c.child(add = -1), c.child(), c.end],
           [],
           [c.beg, 'Jimmy', c.bid],
           ['Jimmy', c.bid],
           ['Jimmy', c.bid, c.mon, c.mag],
           ['Jimmy', c.bid, c.bug],
           ['Jimmy', c.bid, c.franj],
           ['Jimmy', c.bid],
           ['Jimmy', c.bid, c.mau, c.end],
           [],
           [c.beg, c.pen, c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.end],
           [c.beg, c.ceb], # caricatura da mônica no pc entra? (feito pelo cebolinha)
           [c.ceb, c.mon, c.san, c.blo, c.end], # mônica e sansão na foto recebida pelo cebolinha no pc
           [c.beg, c.nim],
           [c.nim, c.cas],
           [c.nim, c.cas, c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim()],
           [c.nim, c.cas],
           [c.nim, c.cas],
           [c.nim, c.cas, c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.anim()],
           [c.nim, c.cas, c.fig(), c.fig(), c.fig(), c.fig(), c.anim(), c.fig(), c.fig(), c.fig(), c.anim(), c.fig()],
           [c.nim, c.cas, c.mcas, c.end],
           [c.beg, c.hum, 'Eco', c.end]] # o eco fala, incluir ele?
