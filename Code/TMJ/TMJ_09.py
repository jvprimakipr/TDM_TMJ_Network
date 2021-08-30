from Functions.class_TM import TM
from Functions.class_characters import characters
c = characters('#1tmj_09')
cap1 = [[c.beg, c.mon, c.ceb, c.toni, c.end], #Capa - O Príncipe Perfeito
        [], [], [], [c.beg, c.xav, c.stu()], #1. A Audição - Pág 5 
        [c.xav, c.jor, c.stu(1), c.stu()] + c.crowd(figs=0, shades=5),
        [c.xav, c.jor, c.stu(1), c.stu(2)] + c.crowd(1),
        [c.mon, c.jor],
        [c.mon, c.mag, c.xav, c.stu(1)],
        [2, [c.mon, c.mag, c.cas], [c.mon, c.ceb]],
        [c.mon, c.mag],
        [c.mon, c.mag, c.den, c.carfru],
        [c.mon, c.mag, c.den, c.carfru],
        [c.mon, c.mag, c.den, c.carfru, c.jor],
        [c.mon, c.cas, c.jor],
        [c.mon, c.cas, c.san],
        [c.mon, c.cas],
        [c.mon, c.mag, c.cas, c.jor, c.san],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.cas, c.xav, c.jor],
        [c.ceb, c.mag, c.den, c.carfru, c.xav, c.jor],
        [c.mon, c.ceb, c.den, c.carfru],
        [c.mon, c.ceb, c.mag, c.cas, c.den, c.carfru, c.xav, c.jor],
        [c.mon, c.ceb, c.mag, c.cas, c.carfru, c.xav, c.jor],
        [c.ceb, c.den, c.carfru, c.xav],
        [c.mon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.mag],
        [c.mon, c.mag, c.toni],
        [c.mon, c.mag, c.toni],
        [c.mon, c.mag, c.toni],
        [c.ceb, c.cas, c.mceb],
        [c.ceb, c.cas, c.mceb, c.pceb],
        [c.ceb, c.cas],
        [c.mon, c.ceb, c.cas],
        [c.ceb, c.cas, c.pceb],
        [c.mon, c.end]]
cap2 = [[c.beg, c.mon, c.toni], #2. Tonc - Pág 41
        [c.mon, c.ton],
        [c.ceb, c.cas],
        [c.ceb, c.cas, c.xav],
        [c.mon, c.ceb, c.cas] + c.crowd(figs=0, stus=10),
        [c.mon, c.ceb, c.den, c.carfru, c.toni],
        [c.mon, c.ceb, c.mag, c.den, c.carfru, c.toni],
        [c.mon, c.ceb, c.toni],
        [c.mon, c.ceb, c.mag, c.cas, c.den, c.carfru, c.toni] + c.crowd(2),
        [2, [c.toni, c.fig()], [c.mon, c.mag, c.toni]],
        [2, [c.xav, c.toni] + c.figs(3) + c.shades(5), [c.ceb, c.toni]],
        [c.mon, c.ceb, c.mag, c.cas, c.toni],
        [c.mon, c.mag, c.carfru, c.toni],
        [c.mon, c.ceb, c.den, c.carfru, c.toni],
        [c.mon, c.ceb, c.cas, c.toni],
        [c.ceb, c.cas, c.toni, c.rub] + c.crowd(2),
        [c.ceb, c.den, c.carfru, c.toni, c.rub],
        [c.mon, c.ceb, c.mag, c.cas, c.toni, c.stu()] + c.shades(10),
        [c.mon, c.mag, c.xav] + c.crowd(figs=0, stus=7),
        [c.mon, c.mag, c.cas, c.toni],
        [c.mon, c.mag, c.toni],
        [c.mon, c.toni],
        [c.mon, c.ceb, c.mag, c.toni],
        [c.mon, c.ceb, c.mag, c.toni],
        [c.den, c.carfru, c.xav, c.doc, c.jor],
        [c.mon, c.mag, c.toni],
        [c.mon, c.ceb, c.mag, c.carfru, c.toni],
        [c.mon, c.ceb, c.cas, c.xav, c.toni],
        [c.ceb, c.xav, c.toni],
        [c.xav, c.toni],
        [c.xav, c.toni],
        [c.mon, c.ceb, c.mag, c.cas, c.xav, c.toni],
        [c.ceb, c.xav, c.toni, c.jor],
        [c.mon, c.mag, c.carfru, c.xav, c.toni, c.jor],
        [c.mon, c.ceb, c.den, c.carfru, c.toni] + c.shades(3),
        [c.mon, c.ceb, c.toni],
        [c.mon, c.ceb, c.toni, c.fig(), c.shade()],
        [c.mon, c.ceb, c.mar, c.toni, c.anim()],
        [c.ceb, c.cas, c.toni],
        [c.mon, c.ceb, c.toni] + c.shades(5),
        [c.ceb, c.end]]
cap3 = [[c.beg, c.mon, c.ceb, c.carfru, c.toni], #3. A Escolha - Pág 83
        [c.ceb, c.cas, c.den, c.carfru, c.xav, c.toni, c.jor],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.cas, c.toni, c.jor],
        [c.ceb, c.cas, c.jor],
        [c.ceb, c.mag, c.cas, c.den, c.xav],
        [c.mon, c.ceb, c.mag, c.cas, c.den, c.toni, c.jor],
        [c.den, c.carfru, c.xav, c.toni, c.jor],
        [c.mon, c.mag, c.den, c.toni, c.jor],
        [c.mon, c.toni],
        [c.ceb, c.mmon, c.pmon, c.jor] + c.crowd(),
        [c.ceb, c.den, c.toni, c.stu(1)],
        [c.mon, c.ceb, c.toni],
        [c.mon, c.ceb, c.cas, c.toni, c.jor],
        [c.mon, c.ceb, c.toni, c.mmon, c.pmon] + c.crowd(4),
        [c.mon, c.mag, c.den, c.xav, c.jor, c.fig()],
        [c.mon, c.mag, c.den, c.toni, c.jor],
        [c.mon, c.mag, c.toni],
        [c.mon, c.mag, c.toni],
        [c.mon, c.toni],
        [c.mon, c.toni],
        [c.mon, c.toni],
        [c.ceb, c.toni],
        [c.ceb, c.toni],
        [c.ceb, c.toni],
        [2, [c.mon, c.ceb, c.cas, c.toni, c.san], [c.ton, 'Pai do Toni', c.child(), c.child()]],
        [c.ceb, c.toni],
        [c.ceb, c.toni],
        [c.ceb, c.toni],
        [c.ceb, c.toni],
        [c.mon, c.ceb, c.mag, c.cas, c.den, c.xav, c.toni, c.jor] + c.figs(3),
        [c.mon, c.mag, c.cas, c.den, c.carfru, c.xav, c.jor, c.fig(add=-1), c.fig(add=0)],
        [c.ceb, c.toni],
        [c.ceb, c.toni],
        [c.mon, c.ceb, c.toni],
        [c.mon, c.ceb, c.toni],
        [c.mon, c.ceb, c.toni, c.san],
        [c.mag, c.cas, c.den, c.fig()],
        [c.mon, c.ceb, c.mag, c.cas],
        [c.mon, c.ceb],
        [c.mon, c.ceb],
        [c.mon, c.ceb, c.toni],
        [c.mon, c.ceb, c.end],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [c.marcas, c.nim]] #4 Capa
        
pages9 = cap1 + cap2 + cap3