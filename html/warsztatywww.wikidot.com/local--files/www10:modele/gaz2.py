#!/usr/bin/env python
import random #zeby losowac zwrot wektora predkosci
import math #sinus,cosinus i pi
import numpy as np #wektory
import matplotlib.pyplot as plt #rysowanie
from matplotlib.patches import Circle #zeby rysowac kolka
class czastka: #ogolnie nie bedziemy uzywac klas, ale tu sie przyda
	def __init__(self,promien,pos,vel): #argumenty podawane przy tworzeniu czastki
		self.promien = promien #czastki to kola o promieniu promien
		self.r=pos #r to dwuwymiarowy wektor postaci [x,y]
		self.v=vel #kolejny dwuwymiarowy wektor, predkosc
		self.deltav=np.array([0.0,0.0]) #o ile ma sie zmienic predkosc w kolejnym kroku symulacji (tez wektor)
N=81 #calkowita liczba czastek
Nx=9 #liczba czastek w 1 wierszu
Ny=9 #liczba czastek w 1 kolumnie
boxsize=20.0 #wymiary pudelka
b2=boxsize/2.0 #polowa boku
dt=0.00001 #krok czasowy
prom=0.4 #promien czastek, ustalilem, ze wszystkie maja ten sam
Tmax=0.01 #czas, po jakim konczy sie symulacja
vsr=250.0 #wartosc predkosci czastek
deltax=boxsize/Nx #poczatkowa pozioma odleglosc miedzy sasiednimi czastkami
deltay=boxsize/Ny #poczatkowa pionowa odleglosc miedzy sasiednimi czastkami
particles = [] #lista czastek
srednieenergie = [] #lista srednich energii w kazdym kroku symulacji
czasy = [] # lista, ktora bedzie postaci 0,dt,2dt,...,Tmax, nie tworze jej na poczekaniu, bo chce aby miala DOKLADNIE tyle samo elementow co lista srednieenergie (potrzebne aby narysowac wykres sredniej energii od czasu Esr(t)

for i in range(Nx): #tworze czastki
	for j in range(Ny):
		polozenie = np.array([(i+0.5)*deltax, (j+0.5)*deltay])
		los=2*math.pi*random.random() #losuje zwrot wektora predkosci
		predkosc=vsr*np.array([math.cos(los),math.sin(los)]) #tworze wektor o dlugosci vsr
		particles.append(czastka(prom,polozenie,predkosc) ) #dodaje do particles[] nowa czastke

t=0.0 #czas na razie jest zero
en=0 #numer kroku symulacji
while t<Tmax: #glowna petla symulacji
	t=t+dt #zwiekszam czas o dt
	if (en%100==0): #bede rysowal obrazek co setny krok symulacji
		plt.clf() #czyszcze wykres (clf=clear figure)
		F = plt.gcf() #biore get current figure
		F.set_size_inches((6,6)) #ustalam rozmiar current figure
		for p in particles: #rysuje wszystkie czastki
			a = plt.gca() #get current axes, niestety zeby narysowac kolko trzeba takich trikowych polecen
			cir = Circle((p.r[0],p.r[1]), radius=p.promien) #tworze kolko
			a.add_patch(cir) #dodaje kolko do current axes
		plt.plot() #rysuje wszystkie kolka
		plt.xlim((0,boxsize)) #obszar wykresu
		plt.ylim((0,boxsize))
		nStr=str(en) #string z numerem kroku...
		nStr=nStr.rjust(5,'0') #... ktory zawsze ma 5 cyfr
		plt.title("Symulacja gazu doskonalego, krok "+nStr) #tytul wykresu
		plt.savefig('img'+nStr+'.png') #zapisuje plik, np. img00100.png dla setnego kroku
		print "Krok "+str(en) #a to sie wyswietli w konsoli
	en=en+1 #zwiekszam krok o 1
	for p in particles: #najwazniejsze, patrze kiedy 2 czastki sie od siebie odbija
		for p2 in particles: #da sie to wydajniej zrobic, ale zlozonosc O(N^2) da sie przezyc
			odl=p2.r-p.r #odleglosc miedzy 2 czastkami, ktora tez jest wektorem!
			if odl[0]>b2: #biore pod uwage, ze przeciwlegle sciany sa sklejone razem
				odl[0]=odl[0]-boxsize
			elif odl[0]<-b2:
				odl[0]=odl[0]+boxsize
			if odl[1]>b2:
				odl[1]=odl[1]-boxsize
			elif odl[1]<-b2:
				odl[1]=odl[1]+boxsize
			r12=np.linalg.norm(odl) #np.linalg.norm(wektor) zwraca dlugosc wektora
			#i tu jest zadanie dla Ciebie: dwie czastki, wektor od p1 do p2 to odl, jego dlugosc to r12,
			#promienie czastek to prom, odbicie jest idealnie sprezyste
			#hint: rzutowanie wektora x na wektor odl to: np.dot(x,odl)/(np.linalg.norm(odl))
			#Ogolnie np.dot(x,y) to iloczyn skalarny x i y
	energie=[] #teraz trzeba policzyc energie i poprzesuwac czastki
	for p in particles:
		p.v=p.v+p.deltav #uaktualniam predkosci
		energie.append(np.dot(p.v,p.v)) #dla uproszczenia zamiast mv^2/2 dodaje po prostu v^2
		p.r=p.r+p.v*dt #przesuwam czastki o v*dt=dr
		p.deltav=np.array([0.0,0.0]) #zeruje dla kazdej czastki deltav
		#Kolejne zadanie dla Ciebie: a co gdy czastka wyjdzie poza pudelko? Musi wyjsc z drugiej strony!
	czasy.append(t) #dodaje czas t do listy czasy
	srednieenergie.append(np.mean(energie)); #licze srednia listy energie[] i dodaje ja do listy srednieenergie

plt.clf()
histogram=dict() #tworze slownik, ktory przechowuje pary klucz-wartosc
energie.sort() #sortuje liste energii
szerokoscslupka=(energie[N-1]-energie[0])/8.0 #ustalam szerokosc 1 slupka histogramu
for e in energie: #dodaje kolejne energie
	ehist=e-e%szerokoscslupka # % to reszta z dzielenia, np. przez 200, tak ze e=1200 i e=1000 obie dadza ehist=1000
	if ehist in histogram: #jesli klucz juz jest...
		histogram[ehist]+=1 #... to zliczam kolejna energie
	else: #... a jesli go nie ma...
		histogram[ehist]=1 #... tworze nowy klucz z wartoscia 1
x = sorted(histogram.keys()) # sortuje po kluczach
y = [ histogram[k] for k in x ] # wartosci zliczen
plt.plot(x,y) # rysuje
plt.xlabel("Energia")
plt.savefig('histogram.png') #i wreszcie mamy histogram

plt.clf() #czas na wykres Esr(t)
plt.plot(czasy,srednieenergie) #na osi X beda czasy, na osi Y srednieenergie - dlatego musza miec tyle samo elementow!
plt.xlabel("czas") #czas na osi poziomej
plt.ylabel("srednia energia") #Esr na pionowej
plt.savefig('sredniaenergia.png') #i zapisuje ostatni wykres (powinno wyjsc Esr=const=vsr^2)

#Na koniec mozesz zrobic gifa z animacja gazu np. linuxowym poleceniem convert img* -delay 20 gaz.gif