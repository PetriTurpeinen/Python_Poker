from tkinter import *
from PIL import ImageTk, Image
import random
import kortti
import pokeri
import pakka

#Create an instance of Tkinter and force the resolution to be 1200x800
root = Tk()
root.title('Korttipeli')
root.geometry("1200x800")

#Initialising the deck
kortti_pakka = []
#Initialising list of the drawn cards
jaetut_kortit = []
temp_jaetut_kortit = []
#kortti_pakka.sort()
#for test purpose to print the deck
#for i in kortti_pakka:
#	print(i.arvo, i.maa)
vaihdetut = 5
pokeri_kasi = StringVar()

# Functions to switch card states when selected
def switch_kortti1():
	if myKortti1_button["state"] == "normal":
		myKortti1_button["state"] = "disabled"
		undoKortti1_button["state"] = "normal"
def switch_kortti2():
	if myKortti2_button["state"] == "normal":
		myKortti2_button["state"] = "disabled"
		undoKortti2_button["state"] = "normal"
def switch_kortti3():
	if myKortti3_button["state"] == "normal":
		myKortti3_button["state"] = "disabled"
		undoKortti3_button["state"] = "normal"
def switch_kortti4():
	if myKortti4_button["state"] == "normal":
		myKortti4_button["state"] = "disabled"
		undoKortti4_button["state"] = "normal"
def switch_kortti5():
	if myKortti5_button["state"] == "normal":
		myKortti5_button["state"] = "disabled"
		undoKortti5_button["state"] = "normal"

def switch_undokortti1():
	if undoKortti1_button["state"] == "normal":
		undoKortti1_button["state"] = "disabled"
		myKortti1_button["state"] = "normal"

def switch_undokortti2():
	if undoKortti2_button["state"] == "normal":
		undoKortti2_button["state"] = "disabled"
		myKortti2_button["state"] = "normal"

def switch_undokortti3():
	if undoKortti3_button["state"] == "normal":
		undoKortti3_button["state"] = "disabled"
		myKortti3_button["state"] = "normal"

def switch_undokortti4():
	if undoKortti4_button["state"] == "normal":
		undoKortti4_button["state"] = "disabled"
		myKortti4_button["state"] = "normal"

def switch_undokortti5():
	if undoKortti5_button["state"] == "normal":
		undoKortti5_button["state"] = "disabled"
		myKortti5_button["state"] = "normal"
		
# Drawing the cards and positioning them on the screen
def draw_cards():
		global myKortti1_button
		global myKortti2_button
		global myKortti3_button
		global myKortti4_button
		global myKortti5_button
		global undoKortti1_button
		global undoKortti2_button
		global undoKortti3_button
		global undoKortti4_button
		global undoKortti5_button
		global kortti_pakka
		global jaetut_kortit
		global vaihdetut
		global kortti_sijainti
		global kortti_sijaint2
		global kortti_sijaint3
		global kortti_sijaint4
		global kortti_sijaint5
		global kortti_kuva1
		global kortti_kuva2
		global kortti_kuva3
		global kortti_kuva4
		global kortti_kuva5

		vaihdetut = 5

		kortti_pakka.clear()
		jaetut_kortit.clear()

		pakka.Pakka.luo_pakka(kortti_pakka)
		pokeri.Pokeri.arvo_kortit(kortti_pakka,jaetut_kortit,vaihdetut)
		pakka.Pakka.tulostus_jaetut_kortit(jaetut_kortit)

		kortti_sijainti = str(jaetut_kortit[0].arvo) + jaetut_kortit[0].maa + ".png"
		kortti_sijainti2 = str(jaetut_kortit[1].arvo) + jaetut_kortit[1].maa + ".png"
		kortti_sijainti3 = str(jaetut_kortit[2].arvo) + jaetut_kortit[2].maa + ".png"
		kortti_sijainti4 = str(jaetut_kortit[3].arvo) + jaetut_kortit[3].maa + ".png"
		kortti_sijainti5 = str(jaetut_kortit[4].arvo) + jaetut_kortit[4].maa + ".png"

		kortti_kuva1 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti))
		kortti_kuva2 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti2))
		kortti_kuva3 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti3))
		kortti_kuva4 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti4))
		kortti_kuva5 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti5))
	
		myKortti1_button = Button(root, image=kortti_kuva1, command=switch_kortti1)
		myKortti2_button = Button(root, image=kortti_kuva2, command=switch_kortti2)
		myKortti3_button = Button(root, image=kortti_kuva3, command=switch_kortti3)
		myKortti4_button = Button(root, image=kortti_kuva4, command=switch_kortti4)
		myKortti5_button = Button(root, image=kortti_kuva5, command=switch_kortti5)
		myKortti1_button.grid(row=0,column=0, padx=20, pady= 20)
		myKortti2_button.grid(row=0,column=1, padx=20)
		myKortti3_button.grid(row=0,column=2, padx=20)
		myKortti4_button.grid(row=0,column=3, padx=20)
		myKortti5_button.grid(row=0,column=4, padx=20)
		undoKortti1_button = Button(root, text="Undo", state="disabled", command=switch_undokortti1 )
		undoKortti1_button.grid(row=3,column=0, pady= 20)
		undoKortti2_button = Button(root, text="Undo", state="disabled", command=switch_undokortti2 )
		undoKortti2_button.grid(row=3,column=1, pady= 20)
		undoKortti3_button = Button(root, text="Undo", state="disabled", command=switch_undokortti3 )
		undoKortti3_button.grid(row=3,column=2, pady= 20)
		undoKortti4_button = Button(root, text="Undo", state="disabled", command=switch_undokortti4 )
		undoKortti4_button.grid(row=3,column=3, pady= 20)
		undoKortti5_button = Button(root, text="Undo", state="disabled", command=switch_undokortti5 )
		undoKortti5_button.grid(row=3,column=4, pady= 20)

		if changeCards_button["state"] == "disabled":
			newGame_button["state"] = "disabled"
			changeCards_button["state"] = "normal"

		pokeri_kasi.set("")
		myLabel = Label(root, textvariable=pokeri_kasi)
		myLabel.grid(row = 4, column = 2)

# Function for changing cards and placing them on the screen

def change_cards():
	global kortti_pakka
	global jaetut_kortit
	global vaihdetut_kortit
	global kortti_sijainti
	global kortti_sijainti2
	global kortti_sijainti3
	global kortti_sijainti4
	global kortti_sijainti5
	global myKortti1_button
	global myKortti2_button
	global myKortti3_button
	global myKortti4_button
	global myKortti5_button	
	global kortti_kuva1
	global kortti_kuva2
	global kortti_kuva3
	global kortti_kuva4
	global kortti_kuva5
	global temp_jaetut_kortit
	global pokeri_kasi

	if myKortti1_button["state"] == "disabled":
		vaihdetut_kortit = 1
		#jaetut_kortit.clear()
		temp_jaetut_kortit.clear()
		pokeri.Pokeri.arvo_kortit(kortti_pakka,temp_jaetut_kortit,vaihdetut_kortit)
		kortti_sijainti = str(temp_jaetut_kortit[0].arvo) + temp_jaetut_kortit[0].maa + ".png"
		kortti_kuva1 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti))
		myKortti1_button = Button(root, image=kortti_kuva1)
		myKortti1_button.grid(row=0,column=0, padx=20, pady= 20)		
#		print(kortti_sijainti)
	#	print(len(kortti_pakka))
		jaetut_kortit[0].arvo = temp_jaetut_kortit[0].arvo
		jaetut_kortit[0].maa = temp_jaetut_kortit[0].maa
#		print(jaetut_kortit[0].arvo, jaetut_kortit[0].maa)
	if myKortti2_button["state"] == "disabled":
		vaihdetut_kortit = 1
		#jaetut_kortit.clear()
		temp_jaetut_kortit.clear()
		pokeri.Pokeri.arvo_kortit(kortti_pakka,temp_jaetut_kortit,vaihdetut_kortit)
		kortti_sijainti2 = str(temp_jaetut_kortit[0].arvo) + temp_jaetut_kortit[0].maa + ".png"
		kortti_kuva2 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti2))
		myKortti2_button = Button(root, image=kortti_kuva2)
		myKortti2_button.grid(row=0,column=1, padx=20, pady= 20)		
#		print(kortti_sijainti2)
	#	print(len(kortti_pakka))
		jaetut_kortit[1].arvo = temp_jaetut_kortit[0].arvo
		jaetut_kortit[1].maa = temp_jaetut_kortit[0].maa
#		print(jaetut_kortit[1].arvo, jaetut_kortit[1].maa)
	if myKortti3_button["state"] == "disabled":
		vaihdetut_kortit = 1
		#jaetut_kortit.clear()
		temp_jaetut_kortit.clear()
		pokeri.Pokeri.arvo_kortit(kortti_pakka,temp_jaetut_kortit,vaihdetut_kortit)
		kortti_sijainti3 = str(temp_jaetut_kortit[0].arvo) + temp_jaetut_kortit[0].maa + ".png"
		kortti_kuva3 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti3))
		myKortti3_button = Button(root, image=kortti_kuva3)
		myKortti3_button.grid(row=0,column=2, padx=20, pady= 20)		
#		print(kortti_sijainti3)
		jaetut_kortit[2].arvo = temp_jaetut_kortit[0].arvo
		jaetut_kortit[2].maa = temp_jaetut_kortit[0].maa
#		print(jaetut_kortit[2].arvo, jaetut_kortit[2].maa)
	#	print(len(kortti_pakka))
	if myKortti4_button["state"] == "disabled":
		vaihdetut_kortit = 1
		#jaetut_kortit.clear()
		temp_jaetut_kortit.clear()
		pokeri.Pokeri.arvo_kortit(kortti_pakka,temp_jaetut_kortit,vaihdetut_kortit)
		kortti_sijainti4 = str(temp_jaetut_kortit[0].arvo) + temp_jaetut_kortit[0].maa + ".png"
		kortti_kuva4 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti4))
		myKortti4_button = Button(root, image=kortti_kuva4)
		myKortti4_button.grid(row=0,column=3, padx=20, pady= 20)		
#		print(kortti_sijainti4)
		jaetut_kortit[3].arvo = temp_jaetut_kortit[0].arvo
		jaetut_kortit[3].maa = temp_jaetut_kortit[0].maa
#		print(jaetut_kortit[3].arvo, jaetut_kortit[3].maa)
	#	print(len(kortti_pakka))
	if myKortti5_button["state"] == "disabled":
		vaihdetut_kortit = 1
		#jaetut_kortit.clear()
		temp_jaetut_kortit.clear()
		pokeri.Pokeri.arvo_kortit(kortti_pakka,temp_jaetut_kortit,vaihdetut_kortit)
		kortti_sijainti5 = str(temp_jaetut_kortit[0].arvo) + temp_jaetut_kortit[0].maa + ".png"
		kortti_kuva5 = ImageTk.PhotoImage(Image.open("kortti_kuvat/"+kortti_sijainti5))
		myKortti5_button = Button(root, image=kortti_kuva5)
		myKortti5_button.grid(row=0,column=4, padx=20, pady= 20)		
#		print(kortti_sijainti5)
		jaetut_kortit[4].arvo = temp_jaetut_kortit[0].arvo
		jaetut_kortit[4].maa = temp_jaetut_kortit[0].maa
#		print(jaetut_kortit[4].arvo, jaetut_kortit[4].maa)
	#	print(len(kortti_pakka))
	if newGame_button["state"] == "disabled":
		newGame_button["state"] = "normal"
		changeCards_button["state"] = "disabled"

	jaetut_kortit.sort()
	print("You have", pokeri.Pokeri.pokeri_saannot(jaetut_kortit))
	pokeri_kasi.set("You have: " + pokeri.Pokeri.pokeri_saannot(jaetut_kortit))
	myLabel = Label(root, textvariable=pokeri_kasi)
	myLabel.grid(row = 4, column = 2)

#Defining buttons used in the game
changeCards_button = Button(root, text="Change cards", state="disabled", command=change_cards)
changeCards_button.grid(row=3,column=6, pady= 20)
newGame_button = Button(root, text="New Game", state="normal", command =draw_cards)
newGame_button.grid(row=3,column=7, pady= 20)

# Necessary to keep program running
root.mainloop()

#TODO
#1. Fixaa bugi, jos antaa saman indeksin useamman kerran. Peli tulostaa tällöin useamman kortin.
#2. Muokkaa Undo-näppäimet sillein että ne eiväy näy, jos tilana on disabled, jos mahdollista.
#3. Lisää highscores graafiseen versioon. Esim isoon tekstiboksiin





