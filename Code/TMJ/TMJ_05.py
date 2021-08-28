from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters()
c.comic_book = '#1tmj_05'
cap1 = [[c.beg, c.mon, c.ceb, c.mag, c.cas, c.tit, c.den, c.end], #Capa - As Aventuras do dia-a-dia
        [], [], [], [], [],
        [c.beg, c.mon, c.ceb, c.mag, c.fig()], #1. Onze coisas que as garotas amam!! - Pág 7
        [c.mon, c.ceb] + c.crowd(figs=0, shades=8),
        [c.mon, c.ceb] + c.crowd(1),
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.mag, c.ire],
        [c.mon, c.ceb, c.mag, c.ire],
        [c.mon, c.ceb, c.mag, c.ire],
        [c.mon, c.ceb, c.mag] + c.figs(4) + c.shades(2),
        [c.mon, c.mag],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.mag],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.san],
        [2, [c.mon, c.ceb, c.san], [c.mon, c.mag]],
        [c.mon, c.mag, c.san],
        [c.mon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.mag, c.mmon],
        [c.mon, c.den, c.marcas],
        [c.mon, c.mag, c.den, c.marcas, c.mmon],
        [c.mon, c.mag, c.den, c.marcas, c.mmon],
        [c.mon, c.mag, c.den, c.marcas, c.mmon],
        [c.mon, c.mag, c.den, c.marcas, c.mmon],
        [c.mmon, c.pmon] + c.figs(4),
        [c.mon, c.mag, c.den, c.marcas, c.mmon, c.shade()],
        [c.mon, c.mag, c.den, c.mmon, c.ID('Cabeleireira'), c.ID('Manicure'), c.ID('Cabeleireiro')],
        [c.mon, c.mag, c.den, c.mmon, c.ID('Massagista')],
        [c.mon, c.den, c.mmon, c.att()],
        [c.mon, c.mag, c.den, c.marcas],
        [c.mon, c.mag, c.den, c.marcas, c.mmon],
        [c.mon, c.mag, c.den, c.marcas, c.att()],
        [c.mon, c.mag, c.den, c.marcas, c.att(add=0)],
        [c.mon, c.mag, c.marcas, c.mmon] + c.figs(2),
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den, c.marcas, c.mmon, c.fig()] + c.shades(3),
        [c.mon, c.mag, c.den, c.marcas, c.mmon],
        [c.mon, c.mag, c.den, c.marcas],
        [c.mon, c.mag, c.mmon] + c.figs(2) + c.shades(3),
        [c.mon, c.mag, c.den, c.marcas, c.mmon],
        [c.mon, c.ceb, c.mag, c.den, c.marcas],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.den],
        [c.mon, c.ceb],
        [c.mag, c.den, c.marcas, c.mmon],
        [c.mon, c.ceb, c.den, c.mmon],
        [c.mon, c.ceb, c.mag, c.den, c.marcas],
        [c.end]]
cap2 = [[c.beg, c.mon, c.mag] + c.figs(2), #2. Os meninos são todos iguais! - Pág 68
        [c.mon, c.mag, c.shade()],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den, c.rub],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.cas],
        [c.mon, c.ceb, c.cas, c.san],
        [c.mon, c.ceb, c.mag, c.cas, c.xav, c.den, c.rub] + c.figs(2),
        [c.mon, c.mag, c.den, c.san],
        [c.mon, c.mag, c.den],
        [c.mon, c.den, c.san],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.den],
        [2, [c.mon, c.mag, c.den], [c.ceb, c.cas, c.tit]],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.san],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mag, c.den],
        [c.mon, c.mag, c.den],
        [c.mon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.ceb],
        [c.mon, c.ceb],
        [c.mon, c.ceb],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.cas, c.tit] + c.crowd(),
        [c.mon, c.ceb, c.cas, c.tit] + c.crowd(2),
        [c.mon, c.cas, c.tit],
        [c.mon, c.ceb, c.cas, c.tit],
        [c.mon, c.ceb, c.cas],
        [2, [c.mon, c.cas], [c.mon, c.ceb, c.mag, c.cas, c.tit, c.den, c.fig(add=-4), c.fig(add=-3), c.fig(add=-2), c.fig(add=-1), c.fig(add=0)] + c.figs(2)],
        [c.mon, c.mag, c.den],
        [c.mon, c.ceb, c.mag, c.cas, c.tit, c.den, c.fig(add=-2), c.fig(add=0), c.end]]
cap3 = [[c.beg, c.ceb, c.cas, c.tit], #3. Pai! Me empresta a chave do carro? - Pág 116
        [c.ceb, c.cas, c.tit, c.pceb],
        [c.ceb, c.cas, c.tit],
        [c.ceb, c.cas, c.tit, c.pceb],
        [c.ceb, c.cas],
        [c.ceb, c.cas, c.tit, c.pceb],
        [c.ceb, c.cas, c.tit, c.pceb],
        [c.ceb, c.cas, c.tit, c.pceb],
        [c.mon, c.ceb, c.cas, c.tit, c.floq],
        [c.ceb, c.cas, c.tit],
        [c.ceb, c.cas],
        [c.cas, c.pcas, c.end],
        [],
        [],
        [],
        [],
        [c.anj]] #4 Capa
        
pages5 = cap1 + cap2 + cap3