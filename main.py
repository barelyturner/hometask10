import random


class Human:

    def __init__(self, human_volume):
        self.human_volume = human_volume

    def humanvolume(self):
        self.human_volume = 0
        return self.human_volume + random.randrange(50, 80)

    # def __str__(self):
    #     return f'Humans volume is: {self.humanvolume()}'


human = Human


class Godzilla:

    def __init__(self, stomachvolume):
        self.stomachvolume = stomachvolume

    def eat(self, _human):
        self.stomachvolume = self.stomachvolume - _human.humanvolume(self)
        if self.stomachvolume < 1000 * 0.9:
            self.eat(_human)
        else:
            print("It's enough")


godzilla = Godzilla(1000)

godzilla.eat(human)



