import string

adatok = []

class Elem:
    def __init__(self, ev, nev, vegyjel, rendszam, felfedezo):
        self.ev: str = ev
        self.nev: str = nev
        self.vegyjel: str = vegyjel
        self.rendszam: int = int(rendszam)
        self.felfedezo: str = felfedezo

    def __str__(self):
        return f"{self.nev} ({self.vegyjel})"


f = open("./14/felfedezesek.csv", "r", encoding="utf-8")
f.readline()  # Első sor átugrás

for sor in f:
    sor_split = sor.strip().split(";")
    adatok.append(
        Elem(
            sor_split[0],
            sor_split[1],
            sor_split[2],
            sor_split[3],
            sor_split[4],
        )
    )

# 3. feladat
print(f"3. feladat: Elemek száma: {len(adatok)}")

# 4. feladat
okor = 0
for i in range(len(adatok)):
    if adatok[i].ev == 'Ókor':
        okor += 1

okor = list(
    filter(lambda x: x.ev == 'Ókor', adatok)
).__len__()

# lambda x: x.ev == 'Ókor'
# def func(x):
#     return x.ev == 'Ókor'

print(f"4. feladat: Felfedezések száma az ókorban: {okor}")

# 5. feladat
felh_vegyjel = ''
while len(felh_vegyjel) <= 0 or\
    len(felh_vegyjel) > 2 \
        or not all(c in string.ascii_lowercase for c in felh_vegyjel.lower()):
    felh_vegyjel = input("5. feladat: Kérek egy vegyjelet! ")


# c in string.ascii_lowercase for c in felh_vegyjel.lower()
# for c in felh_vegyjel.lower():
#     return (c in string.ascii_lowercase)

# 6. feladat
print("6. feladat: Keresés")
megtaltam = False
for i in range(len(adatok)):
    if felh_vegyjel.lower() == adatok[i].vegyjel.lower():
        print(f"\t Az elem vegyjele: {adatok[i].vegyjel}")
        print(f"\t Az elem neve: {adatok[i].nev}")
        print(f"\t Rendszám: {adatok[i].rendszam}")
        print(f"\t Felfedezés éve: {adatok[i].ev}")
        print(f"\t Felfedező: {adatok[i].felfedezo}")
        megtaltam = True

if not megtaltam:
    print("\t Nincs ilyen elem az adatforrásban!")

# 7. feladat
eves_adatok = []
elozo = 0
while not adatok[elozo].ev.isnumeric():
    elozo += 1

for i in range(elozo+1, len(adatok)):
    adat = adatok[i]
    if adat.ev.isnumeric():
        eves_adatok.append(
            int(adat.ev) - int(adatok[elozo].ev)
        )
        elozo = i

print(f"7. feladat: {max(eves_adatok)} év volt a leghosszabb időszak két elem felfedezése között.")

# 8. feladat
print("8. feladat: Statisztika")
evek_dict = {}
for adat in adatok:
    if adat.ev not in evek_dict:
        evek_dict[adat.ev] = 0
    evek_dict[adat.ev] += 1

for kulcs in evek_dict:
    if evek_dict[kulcs] > 3 and kulcs.isnumeric():
        print(f"\t{kulcs}: {evek_dict[kulcs]} db")
