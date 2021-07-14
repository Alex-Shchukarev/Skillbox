# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.simple_numbers = []

    def __iter__(self):
        self.i = 1
        return self

    def get_prime_numbers(self):
        self.i += 1
        for prime in self.simple_numbers:
            if self.i % prime == 0:
                return False
        return True

    def __next__(self):
        while self.i < self.n:
            if self.get_prime_numbers():
                self.simple_numbers.append(self.i)
                return self.i
        else:
            raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10)
for number in prime_number_iterator:
    print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            yield number
            prime_numbers.append(number)





# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def filter_v1(n):
    n = str(n)
    long_num = len(n)
    if long_num < 2:
        return False
    separator = long_num // 2
    first_part = list(n[:separator])
    if long_num % 2 == 0:
        second_part = list(n[separator:])
    else:
        second_part = list(n[separator + 1:])
    lst_first_part = map(int, first_part)
    lst_second_part = map(int, second_part)
    if sum(lst_first_part) == sum(lst_second_part):
        return True
    else:
        return False

def filter_v2(n):
    n = str(n)
    long_num = len(n)
    if long_num < 2:
        return False
    separator = long_num // 2
    first_part = list(n[:separator])
    if long_num % 2 == 0:
        second_part = list(n[separator:])
        second_part = second_part[::-1]
    else:
        second_part = list(n[separator + 1:])
        second_part = second_part[::-1]
    if first_part == second_part:
        return True
    else:
        return False


