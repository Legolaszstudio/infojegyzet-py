from typing import List
LAB_M = 3.280839895

class Hegy:
    def __init__(self, neve, hegyseg, magassag):
        self.neve = neve
        self.hegyseg = hegyseg
        self.magassag = int(magassag)


adatok: List[Hegy] = []

f = open('./Hegyek/hegyekMo.txt', 'r', encoding='utf-8')
f.readline()

for sor in f:
    sor_split = sor.strip().split(';')
    adatok.append(
        Hegy(
            sor_split[0],
            sor_split[1],
            sor_split[2],
        )
    )

f.close()

# 3. feladat
print(f"3. feladat: Hegycsúcsok száma: {len(adatok)} db")

# 4. feladat
mag_sum = sum([
    hegy.magassag for hegy in adatok
])
print(f"4. feladat: Hegycsúcsok átlagos magassága: ", end="")
eredmeny = f"{mag_sum / len(adatok):.2f}".replace('.', ',')
print(f"{eredmeny} m")

# 5. feladat
legnagyobb_hegy = max(
    adatok,
    key=lambda hegy: hegy.magassag
)
print("5. feladat: A legmagasabb hegycsúcs adatai:")
print(f"\tNév: {legnagyobb_hegy.neve}")
print(f"\tHegység: {legnagyobb_hegy.hegyseg}")
print(f"\tMagasság: {legnagyobb_hegy.magassag} m")

# 6. feladat
felh_magassag = input("6. feladat: Kérek egy magasságot: ")
borzsony = list(
    filter(
        lambda hegy: hegy.magassag > int(felh_magassag) and hegy.hegyseg == "Börzsöny",
        adatok
    )
)

print(f"\t{'Nincs' if len(borzsony) == 0 else 'Van'} {felh_magassag}m-nél magasabb hegycsúcs a Börzsönyben!")

# 7. feladat
magasak = list(
    filter(
        lambda hegy: hegy.magassag * LAB_M > 3000,
        adatok
    )
)

print(f"7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {len(magasak)}")

# 8. feladat
print(f"8. feladat: Hegység statisztika")
hegysegek_map = {}
for hegy in adatok:
    if hegy.hegyseg not in hegysegek_map:
        hegysegek_map[hegy.hegyseg] = 0
    hegysegek_map[hegy.hegyseg] += 1

for hegyseg, db in hegysegek_map.items():
    print(f"\t{hegyseg} - {db} db")

# 9. feladat
f = open('./Hegyek/bukk-videk.txt', 'w', encoding='utf-8')
bukki = list(
    filter(
        lambda hegy: hegy.hegyseg == "Bükk-vidék",
        adatok
    )
)

f.write("Hegycsúcs neve;Magasság láb\n")
for hegy in bukki:
    magasag = str(round(hegy.magassag * LAB_M, 1))
    magasag = magasag.split('.0')[0]
    f.write(f"{hegy.neve};{magasag}\n")
f.close()

print("9. feladat: bukk-videk.txt")