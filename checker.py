import requests


class Checker:
    url = 'https://content-watch.ru/public/api/'
    payload = {
        'action': 'CHECK_TEXT',
        'text': '',
        # todo: засекретить
        'key': 'g96Xpx8RUpIq893',
        'ignore': 'http://www.tpsbank.tomsk.ru',
        'test': 1,
    }

    def is_original(self, comment, is_test=0):
        self.payload['text'] = comment
        # self.payload['test'] = is_test  # todo: раскомментировать строчку для реальных данных

        # todo: обработка ошибок (ответа не 200)! Как статуса самого объекта, так и содержимого тела
        response = requests.post(self.url, self.payload)
        answer = response.json()

        # процентная доля оригинальности должна быть больше или равна 70
        is_original = 'no' if answer['error_code'] != 0 or float(answer['percent']) < 70 else 'yes'

        self.payload['text'] = ''
        return is_original
