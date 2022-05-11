from ygo.card import get_all_traps


def get_normal_trap(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_traps(name=name, fname=fname, type='normal', sort=sort,
                         archetype=archetype, banlist=banlist, cardset=cardset,
                         format=format, startdate=startdate, enddate=enddate)


def get_counter_trap(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_traps(name=name, fname=fname, type='counter', sort=sort,
                         archetype=archetype, banlist=banlist, cardset=cardset,
                         format=format, startdate=startdate, enddate=enddate)


def get_cont_trap(name='', fname='', sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='', enddate=''):
    return get_all_traps(name=name, fname=fname, type='continuous', sort=sort,
                         archetype=archetype, banlist=banlist, cardset=cardset,
                         format=format, startdate=startdate, enddate=enddate)
