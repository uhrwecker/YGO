from ygo.card import get_all_spells


def get_normal_spell(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_spells(name=name, fname=fname, type='normal', sort=sort,
                          archetype=archetype, banlist=banlist, cardset=cardset,
                          format=format, startdate=startdate, enddate=enddate)


def get_field_spell(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_spells(name=name, fname=fname, type='field', sort=sort,
                          archetype=archetype, banlist=banlist, cardset=cardset,
                          format=format, startdate=startdate, enddate=enddate)


def get_equip_spell(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_spells(name=name, fname=fname, type='equip', sort=sort,
                          archetype=archetype, banlist=banlist, cardset=cardset,
                          format=format, startdate=startdate, enddate=enddate)


def get_cont_spell(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_spells(name=name, fname=fname, type='Continuous', sort=sort,
                          archetype=archetype, banlist=banlist, cardset=cardset,
                          format=format, startdate=startdate, enddate=enddate)


def get_quick_spell(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_spells(name=name, fname=fname, type='Quick-Play', sort=sort,
                          archetype=archetype, banlist=banlist, cardset=cardset,
                          format=format, startdate=startdate, enddate=enddate)


def get_ritual_spell(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_spells(name=name, fname=fname, type='ritual', sort=sort,
                          archetype=archetype, banlist=banlist, cardset=cardset,
                          format=format, startdate=startdate, enddate=enddate)
