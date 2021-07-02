# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
#
# Part two
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

class LogPars:

    def __init__(self, filename):
        self.file_name = filename
        self.content = {}

    def read_file_line(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                spisok = line.split()
                self.convert_content(spisok)

    def convert_content(self, spisok):
        date, time, req = spisok[0].split('-'), spisok[1].split(':'), spisok[2]
        self.content['year'], self.content['month'], self.content['day'] = date[0][1:], date[1], date[2]
        self.content['hour'], self.content['minute'], self.content['second'] = time[0], time[1], time[2][:-1]
        self.content['req'] = req

    def count_event(self, param='minute', req='NOK'):
        for i in range(len(self.content)):
            if self.content[i]['req'] == req:
                for key in self.content[i]:
                    if key != param:
                        print('['+self.content[i][key])



    def write_rezult(self):
        pass


lp = LogPars('events.txt')
lp.read_file_line()
lp.count_event()
