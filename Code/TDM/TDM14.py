from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#tdm_33') #Capa
pages14 = [[c.beg, c.jot, c.naj, c.dud, c.mag, c.bid, c.mon, c.ceb, c.cas, c.bug, c.anim(), c.min, c.end],
           [],
           [c.cas, c.ceb, c.mot(), c.fat()] + c.figs(7) + c.kids(11),
           [c.beg, c.mmon, c.mon, c.ceb, c.cas, c.att(), c.shade()] + c.kids(4),
           [c.mon, c.cas, c.ceb, c.shade()],
           [c.cas, c.mon, c.ceb, c.mag] + c.kids(2),
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
           [c.mon] + c.crowd(figs=7, name='Flor'),
           [c.mon] + c.crowd(1) + c.crowd(figs=3, name='Flor'),
           [c.mon, c.bid, c.moca],
           [c.mon, c.moca],
           [c.mon, c.san, c.anim(), c.anim()],
           [c.san, c.jot, c.naj],
           [c.san, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj, c.anim()],
           [c.mon, c.jot, c.naj, c.anim(), c.ID('Cadeirão')],
           [c.mon, c.lou, c.fat(), c.mot()] + c.kids(6) + c.shades(5) + [c.end],
           [],
           [], # [c.ceb, c.luc] # passatempo
           [], # [c.manf, c.mmag, c.bid] # correio
           [], # [c.lou, c.mon, c.cas, c.luc, c.min] # correio
           [],
           [c.beg, c.bug, c.bid],
           [c.bug, c.bid, c.ID('Lorde Orelhão')],
           [c.bug, c.bid, c.ID('Lorde Orelhão'), c.ID('Laika')],
           [c.bug, c.bid, c.ID('Pirulito'), c.ID('Paçoquinha')],
           [c.bug, c.bid, c.ID('Paçoquinha'), c.ID('Atropelado'), c.ID('Farofa'), c.ID('Condessa'), c.ID('Filhote 1'), c.ID('Filhote 2'), c.ID('Filhote 3'), c.ID('Filhote 4'), c.ID('Filhote 5'), c.ID('Filhote 6')],
           [c.bug, c.bid, c.ID('Cachorro 1'), c.ID('Cachorro 2')] + [c.ceb, c.floq, c.mon, c.moca, c.mag, c.min, c.franj, c.dor, 'Cachorro da Dorinha'], # a última lista é em pensamento
           [c.bug, c.bid, c.ID('Atropelado'), c.ID('Paçoquinha'), c.ID('Farofa'), c.ID('Lorde Orelhão'), c.ID('Condessa'), c.ID('Filhote 1'), c.ID('Filhote 2'), c.ID('Filhote 3'), c.ID('Filhote 4')] + c.figs(5),
           [c.bug, c.bid, c.manf, c.end],
           [],
           [c.beg, c.mag, c.fig(), c.fig()],
           [c.mag, c.fig(), c.mon, c.mmon, c.end],
           [c.beg, c.mor] + c.crowd(figs=3, name='Homem'),
           [c.mor] + c.crowd(3) + [c.end],
           [],
           [c.beg, c.mon, c.san, c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb],
           [c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb, c.end],
           [c.beg, c.mon, c.san, c.ceb, c.end]]
