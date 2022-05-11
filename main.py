import src.ygo.monster as ym

co = ym.get_xyz_monster()

print(co.search_by_lvl_rank(9).random_card())
