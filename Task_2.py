class Genius:
    def __init__(self, name):
        self.name = name

    def geniy(self):
        return f"{self.name} - Гений"

class LoL(Genius):
    def lol(self):
        return f"{Genius.geniy(self.name)}\nНо его отчислят, если он не будет учит ООП"

me_lol = LoL(Genius("Святослав"))
print(me_lol.lol())
