#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('Я')
my_family.append('Мама')
my_family.append('Папа')
my_family.append('Брат')
print(*my_family)
# список списков приблизителного роста членов вашей семьи
my_family_height = []
my_family_height.append([])
my_family_height.append([])
my_family_height.append([])
my_family_height.append([])
my_family_height[0].append(my_family[0])
my_family_height[0].append(184)
my_family_height[1].append(my_family[1])
my_family_height[1].append(158)
my_family_height[2].append(my_family[2])
my_family_height[2].append(178)
my_family_height[3].append(my_family[3])
my_family_height[3].append(180)
print(*my_family_height)
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f'Рост {my_family_height[2][0]} - {my_family_height[2][1]} cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
print(f'Общий рост моей семьи - {sum} cm')