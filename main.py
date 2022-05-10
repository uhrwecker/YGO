import load
import ygo
from ygo.monster import *
from ygo.collection import card, coll

fp = ygo.get_all_monsters('effect')
data = load.load_list_of_configs(fp)

co = coll.CardCollection(data)
print(co.monsters())