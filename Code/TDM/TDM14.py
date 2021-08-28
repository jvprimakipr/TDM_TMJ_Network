from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm14'

pages14 = [[c.beg, c.jot, c.naj, c.dud, c.mag, c.bid, c.mon, c.ceb, c.cas, c.bug, c.anim(), c.min, c.end],
           [],
           [c.cas, c.ceb, c.mot(), c.fat()] + c.figs(7) + c.kids(11),
           [c.beg, c.mmon, c.mon, c.ceb, c.cas, c.att(), c.shade()] + c.kids(4),
           [c.mon, c.cas, c.ceb] + c.shades(9), # as sombras podem ser do brinquedo também
           [c.cas, c.mon, c.ceb, c.child(), c.child(), c.child()], # uma criança parece muito a magali
           [c.cas, c.mon, c.ceb],
           [c.cas, c.mon, c.ceb, c.mag, c.shade()],
           [c.cas, c.mon, c.ceb, c.mag, c.mmon, c.att()] + c.kids(4),
           [c.cas, c.mon, c.ceb, c.mag, c.san], # sansão???
           [c.mon],
           [c.mon],
           [c.mon, c.cas, c.ceb],
           [c.mon, c.cas, c.ceb],
           [c.mon, c.cas, c.ceb],
           [c.ceb, c.cas, 'Irmãs Cebolinhas', 'Mãe Cebolinha'],
           ['Irmãs Cebolinhas', c.chi, c.mchi],
           ['Irmãs Cebolinhas', c.chi, c.mchi],
           [c.mon, c.cas, c.ceb],
           [c.mon, c.min],
           [c.mon, c.min],
           [c.mon, c.min],
           [c.mon, c.min, c.bug],
           [c.mon, c.bug, 'Senhor Bacon'],
           [c.mon, c.bug, 'Senhor Bacon'],
           [c.mon, c.bug, 'Senhor Bacon', c.mag, c.dud],
           [c.mon, c.dud, c.mag],
           [c.mon, c.dud, c.mag, c.mar],
           [c.mon, c.cb + 'Flor 1', c.cb + 'Flor 2', c.cb + 'Flor 3', c.cb + 'Flor 4', c.cb + 'Flor 5', c.cb + 'Flor 6', c.cb + 'Flor 7'],
           [c.mon, c.cb + 'Flor 1', c.cb + 'Flor 2', c.cb + 'Flor 3', c.cb + 'Flor 4', c.cb + 'Flor 5', c.cb + 'Flor 6', c.cb + 'Flor 7', c.cb + 'Flor 8', c.cb + 'Flor 9', c.cb + 'Flor 10'],
           [c.mon, c.bid, c.moca],
           [c.mon, c.moca],
           [c.mon, c.san, c.anim(), c.anim()],
           [c.san, c.jot, c.naj],
           [c.san, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj, c.anim()],
           [c.mon, c.jot, c.naj, c.anim(), c.cb + 'Cadeirão'],
           [c.mon, c.lou, c.fat(), c.mot()] + c.kids(6) + c.shades(5) + [c.end],
           [],
           [], # [c.ceb, c.luc] # passatempo
           [], # [c.manf, c.mmag, c.bid] # correio
           [], # [c.lou, c.mon, c.cas, c.luc, c.min] # correio
           [],
           [c.beg, c.bug, c.bid],
           [c.bug, c.bid, c.cb + 'Lorde Orelhão'],
           [c.bug, c.bid, c.cb + 'Lorde Orelhão', c.cb + 'Laika'],
           [c.bug, c.bid, c.cb + 'Pirulito', c.cb + 'Paçoquinha'],
           [c.bug, c.bid, c.cb + 'Paçoquinha', c.cb + 'Atropelado', c.cb + 'Farofa', c.cb + 'Condessa', c.cb + 'Filhote 1', c.cb + 'Filhote 2', c.cb + 'Filhote 3', c.cb + 'Filhote 4', c.cb + 'Filhote 5', c.cb + 'Filhote 6'],
           [c.bug, c.bid, c.cb + 'Cachorro 1', c.cb + 'Cachorro 2'] + [c.ceb, c.floq, c.mon, c.moca, c.mag, c.min, c.franj, c.dor, 'Cachorro da Dorinha'], # a última lista é em pensamento
           [c.bug, c.bid, c.cb + 'Atropelado', c.cb + 'Paçoquinha', c.cb + 'Farofa', c.cb + 'Lorde Orelhão', c.cb + 'Condessa', c.cb + 'Filhote 1', c.cb + 'Filhote 2', c.cb + 'Filhote 3', c.cb + 'Filhote 4'] + c.figs(5),
           [c.bug, c.bid, c.manf, c.end],
           [],
           [c.beg, c.mag, c.fig(), c.fig()],
           [c.mag, c.fig(), c.mon, c.mmon, c.end],
           [c.beg, c.mor, c.cb + 'Homem 1', c.cb + 'Homem 2', c.cb + 'Homem 3'],
           [c.mor, c.cb + 'Homem 3', c.cb + 'Homem 2', c.cb + 'Homem 1', c.end],
           [],
           [c.beg, c.mon, c.san, c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb],
           [c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb, c.end],
           [c.beg, c.mon, c.san, c.ceb, c.end]]
