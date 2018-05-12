import json
import codecs
import os
from checker import Checker
from tomita_executor import Executor
import bs4  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# filepath = 'data-raw/'
original_filepath = 'original/'
# nonoriginal_filepath = 'nonoriginal/'

# checker = Checker()
# for filename in filenames:
#     print(filename)
#     file = (codecs.open(filepath + filename, 'r', encoding='utf-8-sig'))
#     comment_raw = file.read()
#     file.close()
#     comment_pure = json.loads(comment_raw, strict=False)

#     comment_pure['original'] = checker.is_original(comment_pure['text'])
#     if comment_pure['original'] == 'yes':
#         file = open(original_filepath + filename, 'w+')
#         json.dump(comment_pure, file)
#     else:
#         file = open(nonoriginal_filepath + filename, 'w+', encoding='utf-8')
#         json.dump(comment_pure, file)
#

# filenames = os.listdir(original_filepath)
# filenames = ['1_2.txt']
# for filename in filenames:
    # parser.execute(filename)
   # file = (codecs.open(original_filepath + filename, 'r', encoding='utf-8-sig'))
   #  file = (codecs.open(original_filepath + filename, 'r', encoding='utf-8-sig'))
   #  comment_raw = file.read()
   #  file.close()
   #  comment_pure = json.loads(comment_raw, strict=False)
   #  file = open(filename, 'w+', encoding='utf-8')
   #  file.write(comment_pure['text'])
#     file.close()

# <SignificantWord><Value val="СОТРУДНИК"/></SignificantWord> -- sp4 хранит в итоге имена атрибутов в lowercase
values = {}
page = 'facts.txt'
parser = Executor()
filenames = os.listdir(original_filepath)
for filename in filenames:
    parser.execute(filename)
    file = open(page, 'r', encoding='utf-8-sig')
    data = file.read()
    soup = bs4.BeautifulSoup(data, 'lxml')
    file.close()

    raw_values = soup("value")
    for raw_value in raw_values:
        value = raw_value.get('val')
        if value in values:
            values[value] += 1
        else:
            values[value] = 1

print('yaay!')
