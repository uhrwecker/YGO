import ygo
import ygo.monster as ym

co = ym.get_xyz_monster()# ygo.load_collection("./11-May-2022_14-27-40.json")
print(co.id)

print(co.search_by_lvl_rank(9).sort(by='atk'))
cm = co.search_by_lvl_rank(9).sort(by='atk')
#cm.collection[0].download_image()
cm.view()