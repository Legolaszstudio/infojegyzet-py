from datetime import datetime
from typing import List

class TagAllam:
    def __init__(self, nev: str, datum: str) -> None:
        self.nev = nev
        self.datum: datetime = datetime.strptime(datum, '%Y.%m.%d')


f = open('EUcsatlakozas.txt', 'r', encoding='utf-8')
adatok: List[TagAllam] = []
for sor in f:
    adat_split = sor.strip().split(';')
    adatok.append(TagAllam(adat_split[0], adat_split[1]))

f.close()


# 3.
count = 0
for adat in adatok:
    if adat.datum.year < 2018:
        count += 1

print(f"3. feladat: EU tagállamainak száma: {count} db")

# 4.
count = 0
for adat in adatok:
    if adat.datum.year == 2007:
        count += 1
print(f"4. feladat: 2007-ben {count} ország csatlakozott.")

# 5.
mo = list(filter(
    lambda x: x.nev == "Magyarország",
    adatok
))[0]
print(f"5. feladat: Magyarország csatlakozásának dátuma: {mo.datum.strftime('%Y.%m.%d')}")

# 6.
majus_csatl = False
for adat in adatok:
    if adat.datum.month == 5:
        majus_csatl = True
        break

if majus_csatl:
    print("6. feladat: Májusban volt csatlakozás!")
else:
    print("6. feladat: Májusban NEM volt csatlakozás!")

# 7.
maxos_orszag = max(adatok, key=lambda x: x.datum)
print(f"7. feladat: Legutoljára csatlakozott ország: {maxos_orszag.nev}")

# 8.
print("8. feladat: Statisztika")
evek = {}
for adat in adatok:
    if adat.datum.year not in evek:
        evek[adat.datum.year] = 0
    evek[adat.datum.year] += 1

for ev in evek:
    print(f"\t{ev} - {evek[ev]} ország")