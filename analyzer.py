import os
import bs4
from plagiarism_checker import Checker
from tomita_executor import Executor
from mp_stemmer import Stemmer


class Analyzer:
    secret_key = ''
    payload = {
        'rawDataDir': 'data-raw/',
        'originalTextsDir': 'original/',
        'nonoriginalTextsDir': 'nonoriginal/',
        'TomitaOutput': 'facts.txt',
        'MPStemmerOutput': 'stems.txt',
    }
    words = {}

    def __init__(self, secret_key, payload=None):
        self.secret_key = secret_key
        if payload:
            for key, entry in self.payload.items():
                if key in payload:
                    self.payload[key] = payload[key]

    # Отделяем в комментариях оригиналы от шаблонов
    def categorize_texts(self):
        checker = Checker(self.secret_key)
        filenames_to_check = os.listdir(self.payload['rawDataDir'])
        for filename in filenames_to_check:
            with open(self.payload['rawDataDir'] + filename, 'r', encoding='utf-8') as file:
                comment = file.read()
            # процентная доля оригинальности должна быть больше или равна 70
            # При установке is_test=1 с сервера приходят случайно сгенерированный показатель оригинальности текста
            text_is_original = checker.is_original(comment, percentage=70, is_test=1)
            directory = self.payload['originalTextsDir'] if text_is_original else self.payload['nonoriginalTextsDir']
            if not os.path.exists(directory):
                os.makedirs(directory)
            file = open(directory + filename, 'w+', encoding='utf-8')
            file.write(comment)
            file.close()

    # Выделяем список наиболее частотных слов в отзывах
    def calculate_word_references(self, prev_filename):
        parser = Executor(prev_filename)
        filenames = os.listdir(self.payload['originalTextsDir'])
        for filename in filenames:
            parser.execute(filename)
            with open(self.payload['TomitaOutput'], 'r', encoding='utf-8-sig') as file:
                data = file.read()
                soup = bs4.BeautifulSoup(data, 'lxml')
            # В результирующем файле слова хранятся в элементе следующего формата:
            # <SignificantWord><Value val="СОТРУДНИК"/></SignificantWord>
            # Так как тег <Value> не встречается больше ни в каких элементах, то искать нужные слова можно сразу по нему
            # + sp4 преобразует имена элементов в lowercase
            tags = soup("value")
            for tag in tags:
                word = tag.get('val')
                if word in self.words:
                    self.words[word] += 1
                else:
                    self.words[word] = 1

    def write_stem_references(self):
        # Используем стеммер Портера для русского языка для группировки слов по корню
        stemmer = Stemmer()
        stemmer.process(self.words)
        stemmer.print_to_file(self.payload['MPStemmerOutput'])
