class Animal:
    def __init__(self, eat, weight, voice, name):
        self.eat = eat  # кг
        self.weight = weight  # kg
        self.voice = voice
        self.name = name

    def eating(self, time):
        return self.eat * time  # кол-во еды * кол-во кормлений

    def weighing(self, new_weight):
        self.weight = new_weight  # новый вес после взвешивания


class Poultry(Animal):
    egg = 1

    def collect_eggs(self, quantity):
        return self.egg * quantity


class Cattle(Animal):
    milk = 0  # l

    def milking(self, time):
        return self.milk * time


class Geese(Poultry, Animal):
    voice = 'Quack'


class Cow(Cattle, Animal):
    voice = 'Muu'
    milk = 15


class Sheep(Animal):
    voice = 'Bee'
    wool = 15  # kg

    def hair_shearing(self, quantity):
        return self.wool * quantity


class Chicken(Poultry, Animal):
    voice = 'Co-co'

    def collecting_eggs(self, quantity):
        self.egg += quantity


class Goat(Cattle, Animal):
    voice = 'Mee'
    milk = 10


class Duck(Poultry, Animal):
    voice = 'Quack'


geese_one = Geese(1, 2, 'Кря', 'Серый')
geese_two = Geese(1, 2, 'Кря', 'Белый')

cow = Cow(10, 400, 'Мууу', 'Манька')

sheep_one = Sheep(7, 55, 'Бее', 'Барашек')
sheep_two = Sheep(6, 61, 'Бее', 'Кудрявый')

chicken_one = Chicken(2, 1, 'Кудах', 'Ко-Ко')
chicken_two = Chicken(2, 1, 'Кудах', 'Кукареку')

goat_one = Goat(3, 80, 'Мее', 'Рога')
goat_two = Goat(3, 90, 'Мее', 'Копыта')

duck = Duck(2, 3, 'Кря', 'Кряква')

# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

animals_dict = {geese_one.name: geese_one.weight, geese_two.name: geese_two.weight, cow.name: cow.weight,
                sheep_one.name: sheep_one.weight, sheep_two.name: sheep_two.weight,
                chicken_one.name: chicken_one.weight, chicken_two.name: chicken_two.weight,
                goat_one.name: goat_one.weight, goat_two.name: goat_two.weight, duck.name: duck.weight}

count = 0
for weight_animal in animals_dict.values():
    count += weight_animal
print('Общий вес животных', count, 'килограммов')

max_count = 0
animal_id = 0
for i, y in animals_dict.items():
    if max_count < y:
        max_count = y
        animal_id = i
print(animal_id, 'самое тяжелое животное')
