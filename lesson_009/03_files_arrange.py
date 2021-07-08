# -*- coding: utf-8 -*-

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

import os
import time
import shutil


class RebuildZipDir:

    def __init__(self, file_name, exit_file):
        self.file_name = file_name
        self.file_exit = exit_file
        self.archive = []

    def read_dir(self):
        for root, dirs, files in os.walk(self.file_name):
            for file in files:
                self.make_dict_file(root, file)

    def make_dict_file(self, root, file):
        time_creation = os.path.getctime(root + '\\' + file)
        result = time.gmtime(time_creation)
        self.archive.append({'filename': file, 'root': root, 'year': result.tm_year,
                             'month': result.tm_mon, 'day': result.tm_mday})

    def create_dirs(self):
        buf_dirs = set()
        for line in self.archive:
            buf_dirs.add(self.file_exit + '\\' + str(line['year']) + '\\' + str(line['month']))
        for elem in buf_dirs:
            os.makedirs(elem)

    def copy_file(self):
        for line in self.archive:
            src = line['root'] + '\\' + line['filename']
            dst = self.file_exit + '\\' + str(line['year']) + '\\' + str(line['month'])
            shutil.copy2(src, dst)

# print(os.name)
# print(os.environ['PROCESSOR_LEVEL'])
# print(os.getcwd())
# os.mkdir("test")
# path = r'C:\pytest'
# os.mkdir(path)
# path = r'C:\pytest\2021\07\07'
# os.makedirs(path)
# os.remove('C:\pytest')
# os.startfile(r'C:\Users\Александр\Desktop\Запись на прием.pdf')


rd = RebuildZipDir('icons', 'icons_by_date')
rd.read_dir()
rd.create_dirs()
rd.copy_file()
