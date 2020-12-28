import random


class entity():
    speed = 1
    eat = 1
    def __init__(self,parrent=None):
        if parrent != None:
            if random.randint(1,10) <= 2:
                self.speed = parrent.speed + (random.random() / 2)
                self.eat = parrent.eat + (random.random() / 2)
            else:
                self.speed = parrent.speed
                self.eat = parrent.eat


        elif random.randint(1,10) <= 2:
                self.speed = self.speed + (random.random() / 2)
                self.eat = self.eat + (random.random() / 2)


