from ygo.card import get_all_monsters


def get_normal_monster(name='', fname='', type='', attr='', atk=None, deff=None, scale=None,
                       level=0, sort='name', archetype='', banlist='',
                       cardset='', format='', startdate='',
                       enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, scale=scale, level=level, kind='normal',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_effect_monster(name='', fname='', type='', attr='', atk=None, deff=None, scale=None,
                       level=0, sort='name', archetype='', banlist='',
                       cardset='', format='', startdate='',
                       enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, scale=scale, level=level, kind='effect',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_flip_monster(name='', fname='', type='', attr='', atk=None, deff=None, scale=None,
                     level=0, sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='',
                     enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, scale=scale, level=level, kind='flip',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_gemini_monster(name='', fname='', type='', attr='', atk=None, deff=None, scale=None,
                       level=0, sort='name', archetype='', banlist='',
                       cardset='', format='', startdate='',
                       enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, scale=scale, level=level, kind='gemini',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_ritual_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                       level=0, sort='name', archetype='', banlist='',
                       cardset='', format='', startdate='',
                       enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, level=level, kind='ritual',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_toon_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                     level=0, sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='',
                     enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, level=level, kind='toon',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_spirit_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                       level=0, sort='name', archetype='', banlist='',
                       cardset='', format='', startdate='',
                       enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, level=level, kind='spirit',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_tuner_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                      level=0, sort='name', archetype='', banlist='',
                      cardset='', format='', startdate='',
                      enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, level=level, kind='tuner',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_union_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                      level=0, sort='name', archetype='', banlist='',
                      cardset='', format='', startdate='',
                      enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, level=level, kind='union',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_xyz_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                    level=0, sort='name', archetype='', banlist='',
                    cardset='', format='', startdate='',
                    enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, level=level, kind='xyz',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_fusion_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                       level=0, sort='name', archetype='', banlist='',
                       cardset='', format='', startdate='',
                       enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, level=level, kind='fusion',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_synchro_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                        level=0, sort='name', archetype='', banlist='',
                        cardset='', format='', startdate='',
                        enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, level=level, kind='synchro',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)


def get_link_monster(name='', fname='', type='', attr='', atk=None, deff=None,
                     link=0, linkmarker='', linkval=0,
                     level=0, sort='name', archetype='', banlist='',
                     cardset='', format='', startdate='',
                     enddate=''):
    return get_all_monsters(name=name, fname=fname, type=type, attr=attr,
                            atk=atk, deff=deff, link=link, linkmarker=linkmarker,
                            linkval=linkval, level=level, kind='link',
                            sort=sort, archetype=archetype, banlist=banlist,
                            cardset=cardset, format=format, startdate=startdate,
                            enddate=enddate)
