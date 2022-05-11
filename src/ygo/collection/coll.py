import random
import json
from datetime import datetime

from ygo.collection import card


class CardCollection:
    def __init__(self, cards, identifier=''):
        self.collection = [card.Card(**data) for data in cards]
        if not identifier:
            dateTimeObj = datetime.now()
            identifier = dateTimeObj.strftime("%d-%b-%Y_%H-%M-%S")
        self.id = identifier

    def add_card(self, cardd, copy=False):
        if copy:
            return self.collection + [cardd]
        else:
            self.collection.append(cardd)
            return self

    def remove_card(self, cardd, copy=False):
        if type(cardd) == str:
            if cardd in [c.name for c in self.collection]:
                cardd = [c for c in self.collection if c.name == cardd][0]
            else:
                return ValueError(f'No card with name {cardd} in collection.')
        if cardd not in self.collection:
            return ValueError('Card not found in collection.')

        if copy:
            return [c for c in self.collection if c != cardd][0]
        else:
            self.collection.remove(cardd)
            return self

    def sort(self, by='name', reverse=False, copy=False):
        if copy:
            return sorted(self.collection, key=lambda x: getattr(x, by), reverse=reverse)
        else:
            self.collection.sort(key=lambda x: getattr(x, by), reverse=reverse)
            return self

    def save(self, fp='./'):
        data = [c.get_dict() for c in self.collection]
        info = {
            'identifier': self.id,
            'data': data
        }
        with open(fp + self.id + '.json', 'w') as file:
            json.dump(info, file, indent=4)

        return info

    def random_card(self):
        return random.choice(self.collection)

    def view(self):
        import appJar
        import os
        print('Loading images ...')
        path = os.getcwd()
        os.mkdir(path + '/images/')

        image_fp = []
        for c in self.collection:
            image_fp.append(c.download_image(path + '/images/'))

        self.i = 0

        def left():
            if self.i == 0:
                self.i = len(image_fp) - 1
            else:
                self.i -= 1
            app.setImage('simple', image_fp[self.i])

        def right():
            if self.i == len(image_fp) - 1:
                self.i = 0
            else:
                self.i += 1
            app.setImage('simple', image_fp[self.i])

        app = appJar.gui()

        app.startLabelFrame("Cards", 0, 0, colspan=2)
        app.addImage("simple", image_fp[0])
        app.stopLabelFrame()

        app.addButton('<', left, 1, 0, colspan=1)
        app.addButton('>', right, 1, 1, colspan=1)

        app.bindKey("<Right>", right)
        app.bindKey("<Left>", left)

        app.go()

        for item in image_fp:
            os.remove(item)
        os.rmdir(path + '/images/')

    def search_in_description(self, search):
        return CardCollection([data.get_dict() for data in self.collection if search in data.desc])

    def search_by_name(self, id):
        return CardCollection([data.get_dict() for data in self.collection if id in data.name])

    def search_by_archetype(self, id):
        return CardCollection([data.get_dict() for data in self.collection if id in data.archetype])

    def search_by_atk(self, start=None, end=None):
        if not start:
            start = 0
        if not end and not start:
            end = 15000
        if not end and start:
            end = start
        if start > end:
            raise ValueError('Atk range not valid; start bigger than end.')
        return CardCollection([data.get_dict() for data in self.collection if start <= data.atk <= end])

    def search_by_def(self, start=None, end=None):
        if not start:
            start = 0
        if not end and not start:
            end = 15000
        if not end and start:
            end = start
        if start > end:
            raise ValueError('Def range not valid; start bigger than end.')
        return CardCollection([data.get_dict() for data in self.collection if start <= data.deff <= end])

    def search_by_lvl_rank(self, start=None, end=None):
        if not start:
            start = 1
        if not end and not start:
            end = 13
        if not end and start:
            end = start
        if start > end or start < 1 or end > 13:
            raise ValueError()
        return CardCollection([data.get_dict() for data in self.collection if start <= data.level <= end])

    def search_by_linkval(self, start=None, end=None):
        if not start:
            start = 1
        if not end and not start:
            end = 6
        if not end and start:
            end = start
        if start > end or start < 1 or end > 6:
            raise ValueError()
        return CardCollection([data.get_dict() for data in self.collection if start <= data.linkval <= end])

    def search_by_linkmarker(self, marker=''):
        if not marker:
            return self
        else:
            return CardCollection([data.get_dict() for data in self.collection if marker in data.linkmarkers])

    def search_by_attr(self, attr=''):
        if not attr:
            return self
        else:
            return CardCollection([data.get_dict() for data in self.collection if attr.title() == data.attribute])

    def search_by_type(self, type=''):
        if not type:
            return self
        else:
            return CardCollection([data.get_dict() for data in self.collection if type.title() == data.type])

    def monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if data.kind.endswith('onster')])

    def normal_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if data.kind == 'Normal Monster'])

    def tuner_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Tuner' in data.kind])

    def flip_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Flip' in data.kind])

    def toon_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Toon' in data.kind])

    def gemini_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Gemini' in data.kind])

    def spirit_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Spirit' in data.kind])

    def xyz_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Xyz' in data.kind])

    def synchro_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Synchro' in data.kind])

    def fusion_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Fusion' in data.kind])

    def link_monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Link' in data.kind])

    def spells(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Spell' in data.kind])

    def normal_spells(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Normal Spell' == data.kind])

    def quick_play_spells(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Quick' in data.kind])

    def ritual_spells(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Ritual Spell' in data.kind])

    def cont_spells(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Continuous Spell' in data.kind])

    def field_spells(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Field' in data.kind])

    def traps(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Trap' in data.kind])

    def counter_traps(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Counter' in data.kind])

    def cont_traps(self):
        return CardCollection([data.get_dict() for data in self.collection if 'Continuous Trap' in data.kind])

    def __repr__(self):
        i = 0

        line = f'Number of cards in Collection: {len(self.collection)} \n'
        line += '---\n'

        while i < 3 and len(self.collection) > i:
            line += self.collection[i].__repr__()
            line += '\n---\n'
            i += 1

        if i == 3:
            line += f'and {len(self.collection) - i} more ...'

        return line
