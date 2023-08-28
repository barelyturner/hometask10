import random


class Godzilla:

    def __init__(self, stomachvolume=1000, portion=random.randrange(50, 80)):
        self.stomachvolume = stomachvolume
        self.portion = portion
        self.calcvalue = stomachvolume

    def eat(self):
        self.stomachvolume = self.stomachvolume - self.portion
        if self.stomachvolume > self.calcvalue * 0.1:
            print(f'Im still hungry. {self.stomachvolume} liters remained')
            self.eat()
        else:
            print("It's enough")


godzilla = Godzilla()

godzilla.eat()
