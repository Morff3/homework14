class House:

    def __init__(self):
        self.numberOfFloors = 10


Floors = House()
a = 0
step = -1

for i in range(Floors.numberOfFloors, a, step):
    print('Текущий этаж равен:', i)
