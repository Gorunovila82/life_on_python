import random


class entity():
    speed = 1
    eat = 1
    eattmp = 0
    iskilled = False 
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

    def update(self,disteat,eat):
        eattmp = 0 
        eattmp = (self.eat * eat.count)
        print(eattmp)
        if eattmp >= 1 and eattmp < 2:
            return 1

        elif eattmp >= 2:
            return entity(self)
        
        else:
            self.iskilled = True
            return 0






