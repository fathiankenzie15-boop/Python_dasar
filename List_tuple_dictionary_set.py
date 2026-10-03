#list hero ML

nama_hero = ["Layla", "Miya", "Alucard", "Tigreal", "Nana"]
print(nama_hero)
nama_hero.append("Hayabusa")
print(nama_hero)
nama_hero.insert(2, "Fanny")
print(nama_hero)
nama_hero.remove("Nana")
print(nama_hero)
nama_hero.pop(0)
print(nama_hero)
nama_hero.sort()
print(nama_hero)
print(f"Panjang list: {len(nama_hero)}")
print(nama_hero)
#Tuple hero ML
hero_tuple = ("Layla", "Miya", "Alucard", "Tigreal", "Nana")
print(hero_tuple)
print(hero_tuple[2])
print(f"Panjang tuple: {len(hero_tuple)}")
print(hero_tuple)
# hero_tuple.append("Hayabusa")  # ini tidak bisa
# hero_tuple.remove("Nana")      # ini tidak bisa
#dictionary hero ML
kumpulan_hero = {
    "nama": "Hayabusa",
    "role": "Jungler",
    "type": "Assassins",
    "weapon": "Sword",
    "skill": "Quad Shadow"
}
print(kumpulan_hero["nama"])
print(kumpulan_hero["role"])
print(kumpulan_hero["type"])
kumpulan_hero["weapon"] = "Katana"
print(kumpulan_hero)
kumpulan_hero["ultimate"] = "Ougi: Shadow Kill"
print(kumpulan_hero)
# del kumpulan_hero["skill"]  # delete
print(kumpulan_hero)
#Set ML
hero_set = {"Layla", "Miya", "Alucard", "Tigreal", "Nana", "Layla"}
print(hero_set)
hero_set.add("Hayabusa")
print(hero_set)
hero_set.remove("Nana")
print(hero_set)