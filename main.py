import json
import os
from checker import Checker

filepath = 'data-raw/'

filenames = os.listdir(filepath)
# print(filenames)
# filenames = ['14_8.txt']

checker = Checker()

for filename in filenames:
    print(filename)
    file = open(filepath + filename, 'r', encoding='utf-8')
    comment_raw = file.read()
    comment_pure = json.loads(comment_raw, strict=False)
    comment_pure['original'] = checker.is_original(comment_pure['text'])

    print(comment_pure['original'])
