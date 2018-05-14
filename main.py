from analyzer import Analyzer


# данные для работы кода
secret_key = 'A Very Secret Key That You Do Not Want To Compromise'

analyzer = Analyzer(secret_key)
# analyzer.categorize_texts()
analyzer.calculate_word_references()
analyzer.write_stem_references()
