import kortti
import pakka
class Pokeri():
	def pokeri_saannot(pakka):
	    if pakka[0].arvo == 1 and pakka[1].arvo == 10 and pakka[2].arvo == 11 and pakka[3].arvo == 12 and pakka[4].arvo == 13 and pakka[0].maa == pakka[1].maa == pakka[2].maa == pakka[3].maa == pakka[4].maa:
	        kasi = "queen-high straight flush"
	    #Värisuora
	    elif pakka[0].arvo + 1 == pakka[1].arvo and pakka[1].arvo + 1 == pakka[2].arvo and pakka[2].arvo + 1 == pakka[3].arvo and pakka[3].arvo + 1 == pakka[4].arvo and pakka[0].maa == pakka[1].maa == pakka[2].maa == pakka[3].maa == pakka[4].maa:
	        kasi = "straight flush"
	    elif pakka[0].arvo == pakka[1].arvo == pakka[2].arvo == pakka[3].arvo or pakka[1].arvo == pakka[2].arvo == pakka[3].arvo == pakka[4].arvo:
	        kasi = "four of a kind"
	    elif (pakka[0].arvo == pakka[1].arvo == pakka[2].arvo and pakka[3].arvo == pakka[4].arvo) or (pakka[0].arvo == pakka[1].arvo and pakka[2].arvo == pakka[3].arvo == pakka[4].arvo):
	        kasi = "full house"
	    elif pakka[0].maa == pakka[1].maa == pakka[2].maa == pakka[3].maa == pakka[4].maa:
	        kasi = "flush"
	    elif (pakka[0].arvo + 1 == pakka[1].arvo and pakka[1].arvo + 1 == pakka[2].arvo and pakka[2].arvo + 1 == pakka[3].arvo and pakka[3].arvo + 1 == pakka[4].arvo) or \
	                (pakka[0].arvo == 1 and pakka[1].arvo == 10 and pakka[2].arvo == 11 and pakka[3].arvo == 12 and pakka[4].arvo == 13):
	        kasi = "straight"
	    elif (pakka[0].arvo == pakka[1].arvo == pakka[2].arvo) or (pakka[1].arvo == pakka[2].arvo == pakka[3].arvo) or (pakka[2].arvo == pakka[3].arvo == pakka[4].arvo):
	        kasi = "three of a kind"
	    elif (pakka[0].arvo == pakka[1].arvo and pakka[2].arvo == pakka[3].arvo) or (pakka[0].arvo == pakka[1].arvo and pakka[3].arvo == pakka[4].arvo) or (pakka[0].arvo == pakka[2].arvo and pakka[3].arvo == pakka[4].arvo) or (pakka[1].arvo == pakka[2].arvo and pakka[3].arvo == pakka[4].arvo):
	        kasi = "two pairs"
	    elif (pakka[0].arvo == pakka[1].arvo) or (pakka[1].arvo == pakka[2].arvo) or (pakka[2].arvo == pakka[3].arvo) or (pakka[3].arvo == pakka[4].arvo):
	        kasi = "pair"
	    else:
	        kasi = "nothing"
	    return kasi
#Arvotaan viisi kortti korttipakasta (52 korttia) pelaajalle
#vaihdetut oli aikasemmin 5 
	def arvo_kortit(koko_pakka, jaettu_pakka,vaihdetut):
	    for j in range (vaihdetut):
	        testi_kortti = pakka.Pakka.nosta_kortti(koko_pakka)
	        jaettu_pakka.append(kortti.Kortti(testi_kortti.arvo, testi_kortti.maa))
#Funktio, jolla tarkistetaan mikä on käden "arvo" ja funktio palauttaa sen arvon
	def arvon_tarkistus(tarkistus):
		if tarkistus == 'queen-high straight flush':
			kaden_arvo = 10
		elif tarkistus == 'straight flush':
			kaden_arvo = 9
		elif tarkistus == 'four of a kind':
			kaden_arvo = 8
		elif tarkistus == 'full house':
			kaden_arvo = 7
		elif tarkistus == 'flush':
			kaden_arvo = 6
		elif tarkistus == 'straight':
			kaden_arvo = 5
		elif tarkistus == 'three of a kind':
			kaden_arvo = 4
		elif tarkistus == 'two pairs':
			kaden_arvo = 3
		elif tarkistus == 'pair':
			kaden_arvo = 2
		elif tarkistus == 'nothing':
			kaden_arvo = 1
		return kaden_arvo
		