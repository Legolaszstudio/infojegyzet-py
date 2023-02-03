from typing import List
from statistics import mean

class Csapat:
    def __init__(self, nev: str, helyezes, valtozas, pontszam):
        self.nev = nev
        self.helyezes = int(helyezes)
        self.valtozas = int(valtozas)
        self.pontszam = int(pontszam)

adatok: List[Csapat] = []
f = open("fifa.txt", "r", encoding="utf-8")
f.readline() # skip first line
for sor in f:
    split_sor = sor.strip().split(";")
    adatok.append(
        Csapat(
            split_sor[0],
            split_sor[1],
            split_sor[2],
            split_sor[3]
        )
    )
f.close()

# 3. feladat
print(f"3. feladat: A világranglistán {len(adatok)} csapat szerepel")

# 4. feladat
atlagos = mean([csapat.pontszam for csapat in adatok])
atlagos = f"{atlagos:.2f}".replace('.', ',')
print(f"4. feladat: A csapatok átlagos pontsáma: {atlagos} pont")

# 5. feladat
max_valtozas = max(adatok, key=lambda csapat: csapat.valtozas)
print(f"5. feladat: A legtöbbet javító csapat:")
print(f"\tHelyezés: {max_valtozas.helyezes}")
print(f"\tCsapat: {max_valtozas.nev}")
print(f"\tPontszám: {max_valtozas.pontszam}")

# 6. feladat
mo = list(
    filter(lambda csapat: csapat.nev == "Magyarország", adatok)
)
if len(mo) == 0:
    print("6. feladat: A csapatok között nincs Magyarország")
else:
    print("6. feladat: A csapatok között van Magyarország")

# 7. feladat
valtozas_count = {}
for adat in adatok:
    if adat.valtozas not in valtozas_count:
        valtozas_count[adat.valtozas] = 0
    valtozas_count[adat.valtozas] += 1

for valtozas in valtozas_count:
    if valtozas_count[valtozas] > 1: print(f"\t{valtozas} helyet változott: {valtozas_count[valtozas]} csapat")