from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 14'

pages14 = [[c.beg, c.jot, c.naj, c.dud, c.mag, c.bid, c.mon, c.ceb, c.cas, c.bug, 'Borboleta', c.min, c.end],
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
           [c.mon, 'Flor 1', 'Flor 2', 'Flor 3', 'Flor 4', 'Flor 5', 'Flor 6', 'Flor 7'],
           [c.mon, 'Flor 1', 'Flor 2', 'Flor 3', 'Flor 4', 'Flor 5', 'Flor 6', 'Flor 7', 'Flor 8', 'Flor 9', 'Flor 10'],
           [c.mon, c.bid, c.moca],
           [c.mon, c.moca],
           [c.mon, c.san, 'Passarinho 1', 'Passarinho 2'],
           [c.san, c.jot, c.naj],
           [c.san, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj],
           [c.mon, c.jot, c.naj, 'Rex'],
           [c.mon, c.jot, c.naj, 'Rex', 'Cadeirão'],
           [c.mon, c.lou, c.fat(), c.mot()] + c.kids(6) + c.shades(5) + [c.end],
           [],
           [], # [c.ceb, c.luc] # passatempo
           [], # [c.manf, c.mmag, c.bid] # correio
           [], # [c.lou, c.mon, c.cas, c.luc, c.min] # correio
           [],
           [c.beg, c.bug, c.bid],
           [c.bug, c.bid, 'Lorde Orelhão'],
           [c.bug, c.bid, 'Lorde Orelhão', 'Laika'],
           [c.bug, c.bid, 'Pirulito', 'Paçoquinha'],
           [c.bug, c.bid, 'Paçoquinha', 'Atropelado', 'Farofa', 'Condessa', 'Filhote 1', 'Filhote 2', 'Filhote 3', 'Filhote 4', 'Filhote 5', 'Filhote 6'],
           [c.bug, c.bid, 'Cachorro 1', 'Cachorro 2'] + [c.ceb, c.floq, c.mon, c.moca, c.mag, c.min, c.franj, c.dor, 'Cachorro da Dorinha'], # a última lista é em pensamento
           [c.bug, c.bid, 'Atropelado', 'Paçoquinha', 'Farofa', 'Lorde Orelhão', 'Condessa', 'Filhote 1', 'Filhote 2', 'Filhote 3', 'Filhote 4'] + c.figs(5),
           [c.bug, c.bid, c.manf, c.end],
           [],
           [c.beg, c.mag, 'Vendedor de Sanduíche', 'Vendedor de Milho'],
           [c.mag, 'Vendedor de Pastel', c.mon, c.mmon, c.end],
           [c.beg, c.mor, 'Homem 1', 'Homem 2', 'Homem 3'],
           [c.mor, 'Homem 3', 'Homem 2', 'Homem 1', c.end],
           [],
           [c.beg, c.mon, c.san, c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb],
           [c.cas, c.ceb],
           [c.mon, c.san, c.cas, c.ceb, c.end],
           [c.beg, c.mon, c.san, c.ceb, c.end]]
