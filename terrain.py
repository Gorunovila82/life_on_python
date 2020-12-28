import random
class element():
    tip = None
    id = 0
    def __init__(self,tip,id):
        self.tip = tip
        self.id = id


class terrain():
    last = 0
    mapp = [[None for x in range(100)] for x in range(100)]
    def __init__(self):
        nom = 0
        for x in range(len(self.mapp)):
            for y in range(len(self.mapp[x])):
                if self.mapp[x][y] == None:
                    rand = random.randint(0,9)
                    if rand  == 3:
                        self.mapp[x][y] = element("food",nom)

                    nom+=1
                    self.last = nom

    def set_entity(self,x,y):
        t = len(self.mapp) - 1
        d = self.mapp[t][len(self.mapp[t]) - 1]
        it = self.last + 1
        self.last = it
        self.mapp[x][y] = element("entity",it)
                