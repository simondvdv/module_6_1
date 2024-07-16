class Animal:
    def __init__(self, name=None, alive=True, fed=False, ):  # Для класса Animal атрибуты alive = True(живой) и fed =
        self.alive = alive  # False(накормленный), name - имя
        self.fed = fed
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

    pass


class Plant:
    def __init__(self, name=None, edible=False):  # False(съедобность), name - индивидуальное название
        self.edible = edible
        self.name = name


class Fruit(Plant):
    def __init__(self, name, edible=True):
        super().__init__(name, edible)
        self.edible = edible


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
