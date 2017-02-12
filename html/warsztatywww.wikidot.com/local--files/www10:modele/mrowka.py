#!/usr/bin/env python
import random
import math
import numpy as np
from PIL import Image  # do rysowania dwuwymiarowych obrazkow

enmax = 200  # 200 krokow symulacji
L = 11       # siatka bedzie LxL
tab = np.ones((L, L))  # tworze macierz LxL wypelniona jedynkami
im = Image.new("RGB", (L, L), "white")  # tworze obraz LxL wypelniony kolorem bialym

print tab  # debug, pokazujacy jak ladnie Python printuje tablice 2D

tab[int(L / 2.0)][int(L / 2.0)] = 0  # stan poczatkowy: srodek tablicy jest czarny, reszta biala
im.putpixel((int(L / 2.0), int(L / 2.0)), (0, 0, 0))  # jak czarny, to rysuje na srodku czarny piksel...
x = int(L / 2.0)  # ... i ustawiam mrowke na srodku
y = int(L / 2.0)

for en in range(enmax):  # petla for po krokach symulacji, od zera do enmax-1
	nStr = str(en)
	nStr = nStr.rjust(5, '0')  # string z 5cyfrowym numerem kroku
	if tab[x][y] == 1:         # jesli jestem na bialym...
		tab[x][y] = 0      # ...zmieniam na czarne...
		im.putpixel((x, L - 1 - y), (0, 0, 0))  # ... i rysuje czarny piksel.
		# (zauwaz L-1-y: w PIL piksele numerowane sa od gory do dolu i od lewej do prawej)
		
		# Teraz wymysl jak skrecic w prawo!
		
	else:
		tab[x][y] = 1  # W przeciwnym razie zmieniam pole na biale...
		im.putpixel((x, L - 1 - y), (255, 255, 255))  # ..rysuje bialy piksel...
		
		#... i skrecam w lewo - jak?
		
	im.save('ant' + nStr + '.png', "PNG")  # Zapisujemy rysunek podajac nazwe i typ!

# potem zrob gifa np. linuxowym poleceniem convert ant* -delay 20 mrowka.gif
# Pamietaj, ze obrazki i gif beda bardzo, bardzo male! Trzeba bedzie je
# powiekszyc zeby zobaczyc pojedyncze piksele.
