import re
reduta = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
tabA = re.findall('a', reduta)
tabE = re.findall('e', reduta)
tabY = re.findall('y', reduta)
tabI = re.findall('i', reduta)
tabO = re.findall('o', reduta)
tabAA = re.findall('ą', reduta)
tabEE = re.findall('ę', reduta)
tabU = re.findall('u', reduta)
tabOO = re.findall('ó', reduta)
print(len(tabA),len(tabE),len(tabY),len(tabI),len(tabO),len(tabAA),len(tabEE),len(tabU),len(tabOO))