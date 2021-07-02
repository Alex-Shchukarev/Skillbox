import zipfile
from operator import itemgetter


class CharStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.stat_convert = []

    def unzip_file(self):
        if zipfile.is_zipfile(self.file_name):   # проверка является ли файл zip
            zip_arh = zipfile.ZipFile(self.file_name, 'r')     # читаем содержимое zip файла
            for filename in zip_arh.namelist():                # читаем список файлов zip архива
                zip_arh.extract(filename)                      # распаковываем
            self.file_name = filename
        else:
            print(f'{self.file_name} не является zip-файлом')

    def ppt(self):
        print(self.stat_convert)

    def collect_for_file(self):                                       # открываем файл и начинаем построчно читать
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_for_line(line=line[:-1])                 # при чтении отбрасываем перевод строки

    def collect_for_line(self, line):                        # собираем словарь частоты встречаемости символов
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def create_table_rezult(self, marker='frequency', rev=False):              # рисуем результирующую таблицу
        print('+{elem:-^20}+'.format(elem='+'))
        print('|{elem1:^9}|{elem2:^10}|'.format(elem1='буква', elem2='частота'))
        print('+{elem:-^20}+'.format(elem='+'))
        self.statistic_sort(marker=marker, rev=rev)
        print('+{elem:-^20}+'.format(elem='+'))

    def statistic_sort(self, marker, rev):                                # сортируем словарь по букве
        for key, val in sorted(self.stat.items()):
            print(f'|{key:^9}|{val:^10d}|')

    def convert_dict(self):            # конвертируем словарь в список словарей для применения разных сортировок
        self.stat_convert = [{'alpha': key, 'frequency': val} for key, val in self.stat.items()]


class SortCharStat(CharStat):

    def statistic_sort(self, marker='frequency', rev=False):
        self.stat_convert = sorted(self.stat_convert, key=itemgetter(marker), reverse=rev)
        for i in range(len(self.stat_convert)):
            print('|{elem1:^9}|{elem2:^10d}|'
                  .format(elem1=self.stat_convert[i]['alpha'], elem2=self.stat_convert[i]['frequency']))


# char_stat = CharStat('voyna-i-mir.txt.zip')
# char_stat.unzip_file()
# char_stat.collect_for_file()
# char_stat.create_table_rezult()
# char_stat.convert_dict()
# char_stat.ppt()

char_stat = SortCharStat('voyna-i-mir.txt.zip')
char_stat.unzip_file()
char_stat.collect_for_file()
char_stat.convert_dict()
char_stat.create_table_rezult(marker='alpha', rev=True)
