import json
import os
from checker import Checker

filepath = 'data-raw/'
original_filepath = 'original/'
nonoriginal_filepath = 'nonoriginal/'

checker = Checker()

filenames = os.listdir(filepath)
for filename in filenames:
    print(filename)
    file = open(filepath + filename, 'r', encoding='utf-8')
    comment_raw = file.read()
    file.close()
    comment_pure = json.loads(comment_raw, strict=False)
    comment_pure['original'] = checker.is_original(comment_pure['text'])
    if comment_pure['original'] == 'yes':
        file = open(original_filepath + filename, 'w+')
        json.dump(comment_pure, file)
    else:
        file = open(nonoriginal_filepath + filename, 'w+', encoding='utf-8')
        json.dump(comment_pure, file)
