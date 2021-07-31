# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import operator
import os
import threading


class TickerVolatility(threading.Thread):

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.ticker_name = ''
        self.volatility = 0

    def run(self):
        price_buf = set()
        with open('trades\\'+self.file_name, 'r', encoding='utf8') as fef:
            for line in fef:
                line = line.strip()
                secide, tradetime, price, quantity = line.split(',')
                if not price.isalpha():
                    self.ticker_name = secide
                    price = float(price)
                    price_buf.add(round(price, 1))
            price_max = max(price_buf)
            price_min = min(price_buf)
            average_price = (price_max + price_min) / 2
            self.volatility = round(((price_max - price_min) / average_price) * 100, 2)


rezult_tv_min, rezult_tv_max = list(), list()
rez_tv_zero, rez_tv = dict(), dict()
list_files = os.listdir('trades')
files_tk = list()
for file in list_files:
    tv_file = TickerVolatility(file)
    files_tk.append(tv_file)

for elem in files_tk:
    elem.start()

for elem in files_tk:
    elem.join()

for elem in files_tk:
    if elem.volatility == 0:
        rez_tv_zero[elem.ticker_name] = elem.volatility
    else:
        rez_tv[elem.ticker_name] = elem.volatility

rezult_tv_min = sorted(rez_tv.items(), key=operator.itemgetter(1), reverse=False)
rezult_tv_max = sorted(rez_tv.items(), key=operator.itemgetter(1), reverse=True)

print('Максимальная волатильность:')
for i in range(3):
    print('{elem1:^7} - {elem2:^8}%'.format(elem1=rezult_tv_max[i][0], elem2=rezult_tv_max[i][1]))
print('Минимальная волатильность:')
for i in range(3):
    print('{elem1:^7} - {elem2:^8}%'.format(elem1=rezult_tv_min[i][0], elem2=rezult_tv_min[i][1]))
print('Нулевая волатильность:')
for key in rez_tv_zero:
    print('{elem1}, '.format(elem1=key), end='')
