# -*- coding: utf-8 -*-

from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.mozg = False

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        if self.mozg:
            self.house.money += 150
        else:
            self.house.money += 50
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 5)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.miska < 30:
            self.buy_miska()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3 and self.house.cat_in_home < 3:
            self.get_cat()
        elif dice == 4 and self.mozg is False:
            self.learn_py()
        elif dice == 5:
            self.clean_home()
        else:
            self.watch_mtv()

    def get_cat(self):
        cprint('{} подобрал кота на улице и назвал его {}'
               .format(self.name, cats[self.house.cat_in_home]), color='green')
        cats[self.house.cat_in_home].house = self.house
        self.house.cat_in_home += 1
        self.buy_miska()

    def buy_miska(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.miska += 50
            cprint('{} купил еды коту'.format(self.name), color='blue')
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_home(self):
        self.fullness -= 20
        self.house.dirty -= 100
        cprint('{} убрался в доме'.format(self.name), color='blue')

    def learn_py(self):
        self.mozg = True
        cprint('{} выучил Пайтон и устроился на хорошую работу'.format(self.name), color='blue')


class House:
    def __init__(self):
        self.food = 50
        self.money = 0
        self.miska = 0
        self.dirty = 0
        self.cat_in_home = 0

    def __str__(self):
        return 'В доме еды {}, денег {}, котов {}, кошачьей еды {}, загрязненность {}'.format(
            self.food, self.money, self.cat_in_home, self.miska, self.dirty)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.house = None

    def eat(self):
        self.fullness += 20
        self.house.miska -= 10
        cprint('{} поел'.format(self.name), color='blue')

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='green')

    def do_dirty(self):
        self.fullness -= 10
        self.house.dirty += 5
        cprint('{} подрал обои'.format(self.name), color='green')

    def act(self):
        if self.fullness == 0:
            cprint('Кот {} умер от голода'.format(self.name), color='red')
            return
        dice = randint(1, 5)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.do_dirty()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

    def __str__(self):
        return 'Кот {}, сытость {}'.format(self.name, self.fullness)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

cats = [
    Cat(name='Tom'),
    Cat(name='Chip'),
    Cat(name='Dail'),
]
my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    if 0 < my_sweet_home.cat_in_home <= 3:
        for i in range(my_sweet_home.cat_in_home):
            cats[i].act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    if 0 < my_sweet_home.cat_in_home <= 3:
        for i in range(my_sweet_home.cat_in_home):
            print(cats[i])
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
