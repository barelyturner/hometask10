import random


class Godzilla:
    STOMACHVOLUME = 1000

    def __init__(self, stomachvolume, portion):
        self.stomachvolume = stomachvolume
        self.portion = portion

    def eat(self):
        self.stomachvolume = self.stomachvolume - self.portion
        if self.stomachvolume > self.STOMACHVOLUME * 0.1:
            print(f'Im still hungry. {self.stomachvolume} liters remained')
            self.eat()
        else:
            print("It's enough")


godzilla = Godzilla(Godzilla.STOMACHVOLUME, random.randrange(50, 80))

godzilla.eat()
