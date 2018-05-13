import re
import os
import pickle
import operator


class Porter:
    PERFECTIVEGROUND = re.compile(u"((ив|ивши|ившись|ыв|ывши|ывшись)|((?<=[ая])(в|вши|вшись)))$")
    REFLEXIVE = re.compile(u"(с[яь])$")
    ADJECTIVE = re.compile(u"(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|ую|юю|ая|яя|ою|ею|ишн|ав|айш|альн|арн|аст|яст|бельн|ебн|ев|ем|енн|еск|ив|ива|ивн|им|ительн|ическ|ичн|лив|н|ов|оват|озн|ом|онн|орн|очн|ск|тельн|уч|чат|чив|ын|яв|яг|ярн)$")
    PARTICIPLE = re.compile(u"((ивш|ывш|ующ)|((?<=[ая])(ем|нн|вш|ющ|щ)))$")
    VERB = re.compile(
        u"((ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|ыло|ено|ят|ует|уют|ит|ыт|ены|ить|ыть|ишь|ую|ю)|((?<=[ая])(ла|на|ете|йте|ли|й|л|ем|н|ло|но|ет|ют|ны|ть|ешь|нно|ану|а|ва|ева|ива|нича|ну|ова|ыва|)))$")
    NOUN = re.compile(
        u"(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я|ость|ост|ек|енок|аг|ал|альон|арад|ариус|ац|аци|ар|ант|бищ|в|енк|ек|иссимус|овик|арь|атор|ач|еж|енок|енько|ент|ень|онок|ер|онк|енк|есс|еств|ец|еч|ечк|из|изм|ик|илк|инк|ир|ист|ит|их|иц|ичк|ишк|аж|ен|ени|енци|ин|ищ|л|н|ни|ник|ниц|няк|ок|он|от|очк|ств|тель|ти|уг|ун|ур|ух|ци|чик|чонок|щик|щин|щиц|ыш|иш|ышек|юг|юшк|янт|ят|ятин|ятор|яци)$")
    RVRE = re.compile(u"^(.*?[аеиоуыэюя])(.*)$")
    DERIVATIONAL = re.compile(u".*[^аеиоуыэюя]+[аеиоуыэюя].*ость?$")
    DER = re.compile(u"ость?$")
    SUPERLATIVE = re.compile(u"(ейше|ейш)$")
    I = re.compile(u"и$")
    P = re.compile(u"ь$")
    NN = re.compile(u"нн$")

    def stem(word):
        word = word.lower()
        word = word.replace(u'ё', u'е')
        m = re.match(Porter.RVRE, word)
        print(word)
        if hasattr(m, 'groups') and m.groups():
            pre = m.group(1)
            rv = m.group(2)
            temp = Porter.PERFECTIVEGROUND.sub('', rv, 1)
            if temp == rv:
                rv = Porter.REFLEXIVE.sub('', rv, 1)
                temp = Porter.ADJECTIVE.sub('', rv, 1)
                if temp != rv:
                    rv = temp
                    rv = Porter.PARTICIPLE.sub('', rv, 1)
                else:
                    temp = Porter.VERB.sub('', rv, 1)
                    if temp == rv:
                        rv = Porter.NOUN.sub('', rv, 1)
                    else:
                        rv = temp
            else:
                rv = temp

            rv = Porter.I.sub('', rv, 1)

            if re.match(Porter.DERIVATIONAL, rv):
                rv = Porter.DER.sub('', rv, 1)

            temp = Porter.P.sub('', rv, 1)
            if temp == rv:
                rv = Porter.SUPERLATIVE.sub('', rv, 1)
                rv = Porter.NN.sub(u'н', rv, 1)
            else:
                rv = temp
            word = pre + rv
        return word

    stem = staticmethod(stem)

    def process(self, words):
        resulting_dict = {}
        for key, value in words.items():
            stem = self.stem(key)
            if stem in resulting_dict:
                resulting_dict[stem] += words[key]
            else:
                resulting_dict[stem] = words[key]

        dictlist = []
        for key, value in resulting_dict.items():
            temp = [key, value]
            dictlist.append(temp)

        dictlist.sort(key=lambda i: i[1], reverse=True)
        with open('test.txt', 'w', encoding='utf-8') as file:
            for record in dictlist:
                file.write(f'\n{record[0]}: {record[1]}\n')
