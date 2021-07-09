# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


MY_EXCEPTIONS = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]
total_carma = 0
num_day = 1

with open('log-file.txt', 'a', encoding='utf8') as ff:
    while total_carma < ENLIGHTENMENT_CARMA_LEVEL:

        def one_day(random_num, num_day):
            if random_num == 13:
                exc_num = randint(0, 5)
                try:
                    raise MY_EXCEPTIONS[exc_num]('Кастомное исключение')
                except IamGodError as exc:
                    print('I\'am god present +10 carma')
                    ff.write(f'Day - {num_day}, raise exception - {exc} - {MY_EXCEPTIONS[exc_num].__name__}\n')
                    return 10
                except DrunkError as exc:
                    print('I many drink alkohol +7 carma')
                    ff.write(f'Day - {num_day}, raise exception - {exc} - {MY_EXCEPTIONS[exc_num].__name__}\n')
                    return 7
                except CarCrashError as exc:
                    print('I crash car -7 carma')
                    ff.write(f'Day - {num_day}, raise exception - {exc} - {MY_EXCEPTIONS[exc_num].__name__}\n')
                    return -7
                except GluttonyError as exc:
                    print('I eat many food +5 carma')
                    ff.write(f'Day - {num_day}, raise exception - {exc} - {MY_EXCEPTIONS[exc_num].__name__}\n')
                    return 5
                except DepressionError as exc:
                    print('I have depression -5 carma')
                    ff.write(f'Day - {num_day}, raise exception - {exc} - {MY_EXCEPTIONS[exc_num].__name__}\n')
                    return -5
                except SuicideError as exc:
                    print('I don\'t want live -10 carma')
                    ff.write(f'Day - {num_day}, raise exception - {exc} - {MY_EXCEPTIONS[exc_num].__name__}\n')
                    return -10
            else:
                carma = randint(1, 7)
                return carma


        random_num = randint(1, 13)
        total_carma += one_day(random_num, num_day)
        print(f'Today is {num_day} day of surka, my_carma {total_carma}')
        num_day += 1


# https://goo.gl/JnsDqu
