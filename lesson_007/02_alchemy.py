# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self):
        self.elem = 'ВОДА'

    def __str__(self):
        return 'Элемент ВОДА'

    def __add__(self, other):
        return Mixed(elem1=self, elem2=other)

class Air:

    def __init__(self):
        self.elem = 'ВОЗДУХ'

    def __str__(self):
        return 'Элемент ВОЗДУХ'

    def __add__(self, other):
        return Mixed(elem1=self, elem2=other)

class Fire:

    def __init__(self):
        self.elem = 'ОГОНЬ'

    def __str__(self):
        return 'Элемент ОГОНЬ'

    def __add__(self, other):
        return Mixed(elem1=self, elem2=other)

class Earth:

    def __init__(self):
        self.elem = 'ЗЕМЛЯ'

    def __str__(self):
        return 'Элемент ЗЕМЛЯ'

    def __add__(self, other):
        return Mixed(elem1=self, elem2=other)

class Storm:

    def __str__(self):
        return 'ШТОРМ'

class Steam:

    def __str__(self):
        return 'ПАР'

class Dust:

    def __str__(self):
        return 'ПЫЛЬ'

class Dirt:

    def __str__(self):
        return 'ГРЯЗЬ'

class Lava:

    def __str__(self):
        return 'ЛАВА'

class Flash:

    def __str__(self):
        return 'МОЛНИЯ'

class Mixed:

    def __init__(self, elem1, elem2):
        self.elem1 = elem1
        self.elem2 = elem2

    def __str__(self):
        if (self.elem1.elem == 'ВОДА' or self.elem2.elem == 'ВОДА') and \
                (self.elem1.elem == 'ВОЗДУХ' or self.elem2.elem == 'ВОЗДУХ'):
            return str(self.elem1) + ' + ' + str(self.elem2) + ' = ' + str(Storm())
        elif (self.elem1.elem == 'ВОДА' or self.elem2.elem == 'ВОДА') and \
                (self.elem1.elem == 'ОГОНЬ' or self.elem2.elem == 'ОГОНЬ'):
            return str(self.elem1) + ' + ' + str(self.elem2) + ' = ' + str(Steam())
        elif (self.elem1.elem == 'ВОДА' or self.elem2.elem == 'ВОДА') and \
                (self.elem1.elem == 'ЗЕМЛЯ' or self.elem2.elem == 'ЗЕМЛЯ'):
            return str(self.elem1) + ' + ' + str(self.elem2) + ' = ' + str(Dirt())
        elif (self.elem1.elem == 'ВОЗДУХ' or self.elem2.elem == 'ВОЗДУХ') and \
                (self.elem1.elem == 'ОГОНЬ' or self.elem2.elem == 'ОГОНЬ'):
            return str(self.elem1) + ' + ' + str(self.elem2) + ' = ' + str(Flash())
        elif (self.elem1.elem == 'ВОЗДУХ' or self.elem2.elem == 'ВОЗДУХ') and \
                (self.elem1.elem == 'ЗЕМЛЯ' or self.elem2.elem == 'ЗЕМЛЯ'):
            return str(self.elem1) + ' + ' + str(self.elem2) + ' = ' + str(Dust())
        elif (self.elem1.elem == 'ЗЕМЛЯ' or self.elem2.elem == 'ЗЕМЛЯ') and \
                (self.elem1.elem == 'ОГОНЬ' or self.elem2.elem == 'ОГОНЬ'):
            return str(self.elem1) + ' + ' + str(self.elem2) + ' = ' + str(Lava())
        else:
            return str(None)


elemental_water = Water()
elemental_air = Air()
elemental_fire = Fire()
elemental_earth = Earth()
stihiy1 = elemental_air + elemental_water
stihiy2 = elemental_air + elemental_air
stihiy3 = elemental_fire + elemental_water
stihiy4 = elemental_earth + elemental_water
stihiy5 = elemental_air + elemental_earth
stihiy6 = elemental_air + elemental_fire
stihiy7 = elemental_earth + elemental_fire
stihiy8 = elemental_fire + elemental_fire
stihiy9 = elemental_earth + elemental_earth
print(stihiy1)
print(stihiy2)
print(stihiy3)
print(stihiy4)
print(stihiy5)
print(stihiy6)
print(stihiy7)
print(stihiy8)
print(stihiy9)

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
