from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm09'

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
          [c.mon, c.ceb, c.mag, c.san, c.anim(), c.anim(), c.anim(), c.anim(), c.anim(), c.end],
          [c.pit, c.mau], # aqui não tem nem título nem fim
          [c.beg, c.pit, c.thu, c.bol, c.dino(), c.anim()],
          [c.pit, c.dino(n = 1), c.anim(add = 0)],
          [c.pit, c.dino(), c.dino(), c.cb + 'Tchako 1'], # considerei tchako como espécie e não nome
          [c.pit, c.cb + 'Tchako 1', c.cb + 'Tchako 2', c.cb + 'Tchako 3', c.cb + 'Tchako 4'],
          [c.pit, c.cb + 'Tchako 1', c.cb + 'Tchako 2', c.cb + 'Gigante'],
          [c.pit, c.cb + 'Gigante', c.cb + 'Tchako 1', c.cb + 'Tchako 2', c.cb + 'Tchako 3'],
          [c.pit, c.cb + 'Gigante', c.cb + 'Tchako 1', c.cb + 'Tchako 2', c.cb + 'Tchako 3'],
          [c.pit, c.cb + 'Gigante', c.cb + 'Tchako 1', c.cb + 'Tchako 2', c.cb + 'Tchako 3', c.cb + 'Tchako 4', c.cb + 'Tchako 5', c.cb + 'Tchako 6', c.cb + 'Tchako 7', c.dino(n = 1)],
          [c.pit, c.cb + 'Gigante', c.cb + 'Tchako 1', c.cb + 'Tchako 2', c.cb + 'Tchako 3', c.cb + 'Tchako 4', c.cb + 'Tchako 5', c.cb + 'Tchako 6', c.cb + 'Tchako 7', c.cb + 'Tchako 8', c.dino(n = 1), c.cb + 'Alienígena', c.dino(), c.fig(), c.fig(), c.fig()],
          [c.pit, c.cb + 'Índio', c.mau, c.ast, c.end],
          [],
          [c.beg, c.mon, c.ceb],
          [c.mon, c.ceb, c.end],
          [c.beg, c.pen, c.cra, c.end],
          [],
          [c.beg, c.cas, c.anj, c.end],
          [c.beg, c.mon],
          [c.mon, c.ceb, c.cas],
          [c.mon, ], #PRIMAKI (gibi 9 == número 28) ver linha 72 também
          [c.mon, c.pmon, c.mmon, c.moca, c.san],
          [c.mon, c.cas, c.ceb, c.san, c.carfru], # cascão e cebolinha só em fala
          [c.mon, c.mag, c.carfru],
          [c.mon, c.luc, c.ceb, c.anim(), c.cb + 'Alfacinho', c.fabbp],
          [c.mon],
          [c.mon, c.mau, c.end], # maurício ficava fazendo as perguntas em quadradinhos no canto superior esquerdo, devo incluir ele?
          [c.beg, c.mon, c.moca, c.luc, c.mag, c.end]] # tirinha final
