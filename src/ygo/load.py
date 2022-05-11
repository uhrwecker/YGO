import requests
import json
import os

from ygo.collection import coll


def load_list_of_configs(fp):
    data = requests.get(fp)
    open('./local.json', 'wb').write(data.content)
    del data
    with open('./local.json') as file:
        data = json.load(file)

    os.remove('./local.json')

    if 'error' in data:
        return []

    else:
        data = data['data']
        cards = []
        for card in data:
            if 'def' in card:
                card['deff'] = card['def']
                del card['def']
            cards.append(card)

        return coll.CardCollection(cards)