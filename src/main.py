import ygo
import ygo.monster as ym

co = ygo.get_all()
cm = co.search_by_archetype('The Weather')
cm.view()