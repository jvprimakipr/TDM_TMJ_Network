from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 9'

pages9 = [[c.beg, c.ceb, c.cas, c.mon, 'Cebolinha do Futuro', c.end],
          [],
          [c.ceb, c.cas, c.mon, 'Cebolinha do Futuro'],
          [c.beg, c.cas, c.ceb],
          [c.cas, c.ceb, c.fat(), c.child(), c.child(), c.child(), c.child(), c.fig(), 'Cebolinha do Futuro'],
          [c.cas, 'Cebolinha do Futuro', c.child()],
          [c.cas, c.ceb, 'Cebolinha do Futuro'],
          [c.ceb, 'Cebolinha do Futuro'],
          [c.ceb, 'Cebolinha do Futuro'],
          [c.ceb, 'Cebolinha do Futuro'],
          [c.ceb, 'Cebolinha do Futuro', 'Filho do Cebolinha do Futuro', 'Franjinha do Futuro', c.child(), c.child(), c.child(), c.child()],
          [c.cas, c.ceb, 'Cebolinha do Futuro'],
          [c.cas, c.ceb, 'Cebolinha do Futuro'],
          [c.cas, c.ceb, 'Cebolinha do Futuro'],
          [c.cas, c.ceb, 'Cebolinha do Futuro', c.pcas],
          [c.child(), c.child(), c.ceb, 'Cebolinha do Futuro', c.mum, c.zvam],
          [c.ceb, 'Cebolinha do Futuro'],
          [c.ceb, 'Cebolinha do Futuro', c.mon, c.san],
          [c.ceb, 'Cebolinha do Futuro', c.mon, c.san],
          [c.ceb, 'Cebolinha do Futuro', c.mon, c.san],
          [c.ceb, 'Cebolinha do Futuro', c.mon, c.mot(), c.child(), c.child()],
          [c.ceb, 'Cebolinha do Futuro', c.mon],
          [c.ceb, 'Cebolinha do Futuro', c.mon, 'Mônica do Futuro', 'Filho do Cebolinha do Futuro', c.end],
          [], # page 24
          [c.beg, c.ceb],
          [c.ceb, c.lou], # louco dentro do computador
          [c.ceb, c.lou],
          [c.ceb, c.lou],
          [c.ceb, c.lou],
          [c.ceb, c.lou],
          [c.ceb, c.lou],
          [c.ceb, c.lou],
          [c.ceb, c.lou, c.end],
          [], # [c.ceb, c.marceb, c.xav, c.mxav] # correio
          [], # [c.ceb, c.cas, c.mon, c.mag, c.dud] # correio
          [], # [c.ast, c.min, c.franj] # passatempo
          [],
          [c.beg, c.mon, c.ceb],
          [c.mon, c.ceb, c.mag, c.san, 'Pássaro', 'Abelha 1', 'Abelha 2', 'Passarinho 1', 'Passarinho 2', c.end],
          [c.pit, c.mau], # aqui não tem nem título nem fim
          [c.beg, c.pit, c.thu, c.bol, 'Mamute Mamu', 'Ratinho'],
          [c.pit, 'Mamute Mamu', 'Ratinho'],
          [c.pit, 'Dinossauro 1', 'Dinossauro 2', 'Tchako 1'], # considerei tchako como espécie e não nome
          [c.pit, 'Tchako 1', 'Tchako 2', 'Tchako 3', 'Tchako 4'],
          [c.pit, 'Tchako 1', 'Tchako 2', 'Gigante'],
          [c.pit, 'Gigante', 'Tchako 1', 'Tchako 2', 'Tchako 3'],
          [c.pit, 'Gigante', 'Tchako 1', 'Tchako 2', 'Tchako 3'],
          [c.pit, 'Gigante', 'Tchako 1', 'Tchako 2', 'Tchako 3', 'Tchako 4', 'Tchako 5', 'Tchako 6', 'Tchako 7', 'Mamute Mamu'],
          [c.pit, 'Gigante', 'Tchako 1', 'Tchako 2', 'Tchako 3', 'Tchako 4', 'Tchako 5', 'Tchako 6', 'Tchako 7', 'Tchako 8', 'Mamute Mamu', 'Alienígena', 'Dinossauro 3', c.fig(), c.fig(), c.fig()],
          [c.pit, 'Índio', c.mau, c.ast, c.end],
          [],
          [c.beg, c.mon, c.ceb],
          [c.mon, c.ceb, c.end],
          [c.beg, c.pen, c.cra, c.end],
          [],
          [c.beg, c.cas, c.anj, c.end],
          [c.beg, c.mon],
          [c.mon, c.ceb, c.cas],
          [c.mon, ], #PRIMAKI (gibi 9 == número 28) ver linhas 70 e 72 também
          [c.mon, c.pmon, c.mmon, c.moca, c.san],
          [c.mon, c.cas, c.ceb, c.san, c.carfru], # cascão e cebolinha só em fala
          [c.mon, c.mag, c.carfru],
          [c.mon, c.luc, c.ceb, 'Marimbondo', 'Alfacinho', 'Fabinho Boa Pinta'], #PRIMAKI
          [c.mon],
          [c.mon, c.mau, c.end], # maurício ficava fazendo as perguntas em quadradinhos no canto superior esquerdo, devo incluir ele?
          [c.beg, c.mon, c.moca, c.luc, c.mag, c.end]] # tirinha final
