from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm18'

pages18 = [[c.beg, c.spa, c.mon, c.mag, c.cas, c.ceb, c.san, c.end],
		   [],
		   [c.mon, c.mag, c.cas, 'Neto do Franjinha'],
		   [c.beg, c.mag, c.franj],
		   [c.mag, c.franj, 'Fran J. Inha', 'Monika Bond', 'Maga Rári'], # os três últimos só em imagem no computador
		   [c.mag, c.franj, 'Monika Bond', 'Maga Rári'], # as duas últimas na tela do computador (imagem)
		   [c.mag, 'Monika Bond', 'Robô carregando malas 1', 'Robô carregando malas 2', 'Abelha', 'Bidutronic'],
		   [c.mag, 'Monika Bond', 'Abelha', 'Bidutronic', c.spa, c.san, 'Robô amarrando cadarço', c.fig()], # coelho é o sansão, mas no futuro
		   [c.mag, 'Monika Bond', 'Abelha', 'Bidutronic', c.att(), c.att()], # os atendentes são robôs
		   [c.mag, 'Monika Bond', 'Abelha', 'Bidutronic', c.att(), c.att(), c.child(), c.child(), c.mot(), c.fat()], # rt para os atendentes
		   [c.mag, 'Monika Bond', 'Abelha', 'Bidutronic', c.spa, c.san],
		   [c.mag, 'Monika Bond', 'Abelha', 'Bidutronic', c.san, c.franj, 'Fran J. Inha'], # franjinha só em imagem no pc
		   ['Fran J. Inha', 'C-bola'],
		   [c.mag, 'Monika Bond', 'Bidutronic', 'Fran J. Inha', 'C-bola'],
		   [c.mag, 'Monika Bond', 'Bidutronic', 'Fran J. Inha', 'C-bola', 'Cecê-boy'],
		   [c.mag, 'Monika Bond', 'Bidutronic', 'Fran J. Inha', 'C-bola', 'Cecê-boy', c.spa, c.san],
		   [c.mag, 'Monika Bond', 'Fran J. Inha', 'C-bola', 'Cecê-boy', c.spa, c.san],
		   [c.mag, 'Monika Bond', 'Bidutronic', 'Fran J. Inha', 'C-bola', 'Cecê-boy'],
		   [c.mag, 'Monika Bond', 'C-bola', 'Cecê-boy'],
		   [c.mag, 'Monika Bond', 'C-bola', 'Cecê-boy', c.spa],
		   [c.mag, 'Monika Bond', 'C-bola', 'Cecê-boy', c.spa],
		   [c.mag, 'Monika Bond', 'C-bola', 'Cecê-boy', c.san],
		   ['Monika Bond', c.san, 'Congue-Congue'],
		   ['C-bola', 'Invasores do Espaço'], # 8 invasores e uma nava mãe
		   ['Cecê-boy', c.anim()] + c.figs(6),
		   [c.mag, 'Maga Rári', 'Fantasmildos'], # 3 fantasmas
		   ['Monika Bond', 'Congue-Congue', c.san],
		   ['C-bola', 'Etê da Nava Mãe', 'Invasores do Espaço'],
		   ['Cecê-boy', c.anim(add = 0), c.fig(), c.fig()],
		   [c.mag, 'Maga Rári', 'Fantasmildos'],
		   [c.spa, c.san, 'Monika Bond'],
		   [c.spa, c.san, 'Monika Bond', 'C-bola', 'Invasores do Espaço'],
		   ['Cecê-boy', 'Maga Rári', c.mag, c.spa, 'Fantasmildos'],
		   [c.mag, c.spa, 'Cecê-boy', 'C-bola', 'Maga Rári', 'Monika Bond'],
		   [c.mag, c.spa, 'Cecê-boy', 'C-bola', 'Maga Rári', 'Monika Bond'],
		   [c.mag, c.spa, 'Cecê-boy', 'C-bola', 'Maga Rári', 'Monika Bond', 'Bidutronic', 'Fran J. Inha'],
		   [c.mag, c.franj, 'Cecê-boy', 'C-bola', 'Maga Rári', 'Monika Bond', 'Bidutronic', 'Fran J. Inha'],
		   [c.mag, c.franj, c.cas, c.ceb, c.mon, c.bid, c.end],
		   [],
		   [], # [c.tin, c.cas] # correio
		   [], # [c.mon, c.ceb, c.mag, c.marcaf] # correio
		   [], # [c.naj, c.mon] # passatempo
		   [],
		   [c.beg, c.chi, 'Onça'],
		   [c.chi, 'Onça', c.anim(), c.end],
		   [c.beg, c.ceb, c.anj, 'Anjo da Guarda do Anjinho', c.end],
		   [],
		   [c.beg, c.mon, c.san, c.ceb, c.cas],
		   [c.mon, c.san, c.ceb, c.cas, 'Cipolino', 'Gastão'],
		   [c.mon, c.ceb, c.cas, 'Cipolino', 'Gastão'],
		   [c.mon, c.ceb, c.cas, 'Cipolino', 'Gastão'],
		   [c.mon, c.ceb, c.cas, 'Cipolino', 'Gastão', c.san, c.end],
		   [c.beg, c.pit],
		   [c.pit, c.zcav, c.dino()], # zcav em pensamento (na real pode ser um esqueleto qualquer)
		   [c.pit, c.dino(add = 0), c.dino(), c.dino(), c.dino()],
		   [c.pit, c.dino(add = 0), c.cb + 'Planta Carnívora'],
		   [c.pit, c.fig(), c.fig(), c.thu, c.dino(add = -1), c.dino(add = -2), c.end], # figurantes são homens das cavernas
		   [c.beg, c.ceb, c.mag, c.mon, c.san, c.cas, c.xav, c.end],
		   [],
		   [c.beg, c.ceb],
		   [c.ceb, c.cas],
		   [c.ceb, c.cas, c.mon, c.san],
		   [c.ceb, c.mon, c.san],
		   [c.ceb, c.mon, c.san],
		   [c.ceb, c.cb + 'Alien Verde - filho', c.cb + 'Alien Verde - mãe', c.end], # a mãe só em voz e o filho só em mão saindo da nave
		   [c.beg, c.nim, c.cas, c.mdoc, c.end],
		   [],
		   []]
