from analyzer import Analyzer


# данные для работы кода
secret_key = 'g96Xpx8RUpIq893'
prevFilename = '9_1.txt'

analyzer = Analyzer(secret_key)
# analyzer.categorize_texts()
analyzer.calculate_word_references(prevFilename)
analyzer.write_stem_references()
