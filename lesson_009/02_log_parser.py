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
    date_time = {'year': 5, 'month': 8, 'day': 11, 'hour': 14, 'minute': 17, 'second': 20}

    def __init__(self, file_name, rez_file, param, event):
        self.file_name = file_name
        self.rez_file = rez_file
        self.param = param
        self.event = event
        self.start_pos = ''
        self.count = 0

    def read_file_line(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                self.cut_to_datetime(line)

    def cut_to_datetime(self, line):
        current_pos = line[:LogPars.date_time[self.param]]
        srv_answer = line[29:].strip()
        if current_pos == self.start_pos:
            if srv_answer == self.event:
                self.count += 1
        elif self.start_pos == '':
            self.start_pos = current_pos
            if srv_answer == self.event:
                self.count += 1
        else:
            self.write_rezult(current_pos, srv_answer)

    def write_rezult(self, current_pos, srv_answer):
        with open(self.rez_file, 'a', encoding='utf8') as fr:
            fr.write(self.start_pos + '] ' + str(self.count) + '\n')
            self.start_pos, self.count = current_pos, 0
            if srv_answer == self.event:
                self.count += 1

    def write_end(self):
        with open(self.rez_file, 'a', encoding='utf8') as fr:
            fr.write(self.start_pos + '] ' + str(self.count) + '\n')


lp = LogPars('events.txt', 'rez-events.txt', 'hour', 'OK')
lp.read_file_line()
lp.write_end()
