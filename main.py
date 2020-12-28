import food
from terrain import terrain
l = []

for x2 in range(100):
    l.append(food.food())
t = terrain()
data = t.mapp
t.set_entity(0,0)
t.set_entity(2,2)
print(data[0][0].id)
print(data[2][2].id)
