import requests


class Checker:
    url = 'https://content-watch.ru/public/api/'
    payload = {
        'action': 'CHECK_TEXT',
        'text': '',
        'key': '',
        'ignore': 'http://www.tpsbank.tomsk.ru',
        'test': 1,
    }

    def __init__(self, key):
        self.payload['key'] = key

    def is_original(self, comment, percentage, is_test=0):
        self.payload['text'] = comment
        self.payload['test'] = is_test

        response = requests.post(self.url, self.payload)
        answer = response.json()

        is_original = False if answer['error_code'] != 0 or float(answer['percent']) < percentage else True
        self.payload['text'] = ''
        return is_original
