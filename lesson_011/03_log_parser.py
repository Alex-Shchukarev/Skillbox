# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

date_time = {'year': 5, 'month': 8, 'day': 11, 'hour': 14, 'minute': 17, 'second': 20}


def generate_events(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        start_pos, counter = '', 0
        for line in file:
            current_pos = line[:date_time['minute']]
            srv_answer = line[29:].strip()
            if current_pos == start_pos:
                if srv_answer == 'NOK':
                    counter += 1
            elif start_pos == '':
                start_pos = current_pos
                if srv_answer == 'NOK':
                    counter += 1
            else:
                yield start_pos, counter
                start_pos, counter = current_pos, 0
                if srv_answer == 'NOK':
                    counter += 1

        yield start_pos, counter


grouped_events = generate_events(file_name='events.txt')
for group_time, event_count in grouped_events:
    print(f'{group_time}] {event_count}')
