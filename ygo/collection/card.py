class Card:
    def __init__(self, id=0, name='', type='', desc='', archetype='',
                 atk=-1, deff=-1, level=0, race='', linkval=0, linkmarkers=[], scale=0,
                 attribute='', card_sets=[], card_images=[], card_prices=[], banlist_info=[]):
        self.id = id
        self.name = name
        self.kind = type
        self.desc = desc
        self.archetype = archetype
        self.atk = atk
        self.deff = deff
        self.level = level
        self.type = race
        self.linkval = linkval
        self.linkmarkers = linkmarkers
        self.scale = scale
        self.attribute = attribute
        self.card_sets = card_sets
        self.card_images = card_images
        self.card_prices = card_prices
        self.banlist_info = banlist_info

    def get_dict(self):
        info = {
            'id': self.id,
            'name': self.name,
            'type': self.kind,
            'desc': self.desc,
            'attribute': self.attribute,
            'archetype': self.archetype,
            'atk': self.atk,
            'deff': self.deff,
            'level': self.level,
            'race': self.type,
            'linkval': self.linkval,
            'linkmarkers': self.linkmarkers,
            'scale': self.scale,
            'card_sets': self.card_sets,
            'card_prices': self.card_prices,
            'banlist_info': self.banlist_info
        }

        return info

    def __repr__(self):
        line = f'Name: {self.name} \n'
        line += f'{self.kind} \n'

        if self.linkval:
            line += f'Link-{self.linkval} \n'
            line += f'Arrow(s): {self.linkmarkers} \n'
        if self.attribute:
            line += f'Level {self.level} \n'
            line += f'Attr: {self.attribute} | Type: {self.type} \n'
            line += f'Atk:  {self.atk} \n'
            line += f'Def:  {self.deff} \n'
        if self.archetype:
            line += f'{self.archetype} Archetype \n'

        if self.desc:
            line += self.desc

        return line