import random

from ygo.collection import card


class CardCollection:
    def __init__(self, cards):
        self.collection = [card.Card(**data) for data in cards]

    def random_card(self):
        return random.choice(self.collection)

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
