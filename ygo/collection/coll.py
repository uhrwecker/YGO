from ygo.collection import card


class CardCollection:
    def __init__(self, cards):
        self.collection = [card.Card(**data) for data in cards]

    def monsters(self):
        return CardCollection([data.get_dict() for data in self.collection if data.kind.endswith('onster')])

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
