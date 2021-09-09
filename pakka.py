import kortti
import random
class Pakka():
	def luo_pakka(koko_pakka):        
	    for i in range(52):
	        if i < 13:
	            koko_pakka.append(kortti.Kortti(1,'hearts'))
	            koko_pakka[i-1].arvo = i+1                
	        elif i < 26:
	            koko_pakka.append(kortti.Kortti(1, 'diamond'))
	            koko_pakka[i-1].arvo = i - 12
	        elif i < 39:
	            koko_pakka.append(kortti.Kortti(1, 'spade'))
	            koko_pakka[i-1].arvo = i - 25
	        elif i < 52:
	            koko_pakka.append(kortti.Kortti(1, 'club'))
	            koko_pakka[i-1].arvo = i - 38
# Nostetaan yksi sattumanvarainen kortti pakasta      
#	def nosta_kortti(pakka):
	def nosta_kortti(pakka):
	    random_numero = random.randint(0, len(pakka) -1)
	    return pakka.pop(random_numero)
# Tulostetaan pelaajan kortit	
	def tulostus_jaetut_kortit(jaettu_pakka):
	    for k in range (5):
	        print("You have: ", "[", k ,  "]", jaettu_pakka[k].arvo, jaettu_pakka[k].maa)
#Poistetaan kortit, jotka halutaan vaihtaa eli kortit, joiden arvo on 0
	def poista_kortit(jaettu_pakka):
	    for m in jaettu_pakka:
	        if m.arvo == 0:
	            jaettu_pakka.remove(m)
	        for m in jaettu_pakka:    
	            if m.arvo == 0:
	                jaettu_pakka.remove(m)
#Vaihdetaan pelaajalle kortit riippuen montako hän haluaa vaihtaa
	def vaihda_kortit(korttien_maara, koko_pakka, jaettu_pakka):
	    if korttien_maara > 0:
	        for q in range (0,korttien_maara):
	            testi_kortti = Pakka.nosta_kortti(koko_pakka)
	            jaettu_pakka.append(kortti.Kortti(testi_kortti.arvo, testi_kortti.maa))