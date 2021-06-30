import zipfile


class CharStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip_file(self):
        if zipfile.is_zipfile(self.file_name):   # проверка является ли файл zip
            zip_arh = zipfile.ZipFile(self.file_name, 'r')     # читаем содержимое zip файла
            for filename in zip_arh.namelist():                # читаем список файлов zip архива
                zip_arh.extract(filename)                      # распаковываем
            self.file_name = filename
        else:
            print(f'{self.file_name} не является zip-файлом')

    def ppt(self):
        print(self.stat)

    def collect_for_file(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_for_line(line=line[:-1])

    def collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def create_table(self):
        print(f'')



char_stat = CharStat('voyna-i-mir.txt.zip')
char_stat.unzip_file()
char_stat.collect_for_file()
char_stat.ppt()
