import requests
import json
import os


def load_list_of_configs(fp):
    data = requests.get(fp)
    open('./local.json', 'wb').write(data.content)
    del data
    with open('./local.json') as file:
        data = json.load(file)

    os.remove('./local.json')

    for item in data['data']:
        print(item)
    return data