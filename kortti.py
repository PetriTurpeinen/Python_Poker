#Luodaan luokka kortin tiedoille
class Kortti():
    def __init__(self, arvo, maa):
        self.arvo = arvo
        self.maa = maa
    def __lt__(self, other):
        return self.arvo < other.arvo    
    