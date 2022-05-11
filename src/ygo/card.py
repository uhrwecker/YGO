from ygo.load import _load_list_of_configs, load_collection
from ygo.constants import *


def get_all(sort='name', kind='', archetype='', banlist='',
            cardset='', format='', startdate='',
            enddate='', return_val='data'):
    fp = BASE
    fp += f'?sort={sort}'

    if kind:
        fp += f'&type={TYP_CONV[kind]}'

    if archetype:
        fp += f'&archetype={archetype}'

    if banlist:
        fp += f'&banlist={banlist}'

    if cardset:
        fp += f'&cardset={cardset}'

    if format:
        fp += f'&format={format}'

    if startdate and enddate:
        fp += f'&startdate={startdate}&enddate={enddate}'

    if return_val == 'data':
        return _load_list_of_configs(fp)
    elif return_val == 'str':
        return fp


def get_all_monsters(kind, name='', fname='', type='', attr='', atk=None, deff=None,
                     link=0, linkmarker='', linkval=0, scale=None,
                     level=0, sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='',
                     enddate=''):
    base = get_all(sort=sort, kind=kind, archetype=archetype, banlist=banlist,
                   cardset=cardset, format=format, startdate=startdate, enddate=enddate,
                   return_val='str')

    if fname and name:
        return ValueError('Do not specify name and fname field.')

    if fname:
        base += f'&fname={fname}'

    if name:
        base += f'&name={name}'

    if type:
        base += f'&race={type.title()}'

    if attr:
        base += f'&attribute={attr}'

    if atk:
        base += f'&atk={atk}'

    if deff:
        base += f'def={deff}'

    if type == 'link':
        if link != 0:
            base += f'&link={link}'
        if linkmarker:
            base += f'&linkmarker={linkmarker}'
        if linkval != 0:
            base += f'&linkval={linkval}'

    if 'pendulum' in type and scale:
        base += f'&scale={scale}'

    if level != 0:
        base += f'&level={level}'

    return _load_list_of_configs(base)


def get_all_spells(name='', fname='', type='', sort='name', archetype='', banlist='',
                   cardset='', format='', startdate='',
                   enddate=''):
    base = get_all(sort=sort, kind='spell', archetype=archetype, banlist=banlist,
                   cardset=cardset, format=format, startdate=startdate, enddate=enddate,
                   return_val='str')

    if fname and name:
        return ValueError('Do not specify name and fname field.')

    if fname:
        base += f'&fname={fname}'

    if name:
        base += f'&name={name}'

    if type:
        base += f'&race={type.title()}'

    return _load_list_of_configs(base)


def get_all_traps(name='', fname='', type='', sort='name', archetype='', banlist='',
                   cardset='', format='', startdate='',
                   enddate=''):
    base = get_all(sort=sort, kind='trap', archetype=archetype, banlist=banlist,
                   cardset=cardset, format=format, startdate=startdate, enddate=enddate,
                   return_val='str')

    if fname and name:
        return ValueError('Do not specify name and fname field.')

    if fname:
        base += f'&fname={fname}'

    if name:
        base += f'&name={name}'

    if type:
        base += f'&race={type.title()}'

    return _load_list_of_configs(base)


def get_all_archetypes():
    fp = 'https://db.ygoprodeck.com/api/v7/archetypes.php'

    return _load_list_of_configs(fp)


def get_all_cardsets():
    fp = 'https://db.ygoprodeck.com/api/v7/cardsets.php'

    return _load_list_of_configs(fp)