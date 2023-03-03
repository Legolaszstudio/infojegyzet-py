from typing import List


class Szemelyi:
    def __init__(self, nem, ev, honap, nap, egyedi_azon, checksum, raw):
        self.no = (nem == '2' or nem == '4')
        self.ferfi = not self.no

        self.szul_ev = ("19" if (nem == '1' or nem == '2') else "20")
        self.szul_ev += ev
        self.szul_ev = int(self.szul_ev)

        self.honap: int = honap
        self.nap: int = nap

        self.egyedi_azon = egyedi_azon
        self.checksum = checksum

        self.raw = raw


def CdvEll(azon):
    provided_checksum = int(azon[-1])

    szamsor = azon.replace('-', '')[:-1]
    szamok = [
        int(szamsor[i]) * (10-i) for i in range(len(szamsor))
    ]
    osszeg = sum(szamok)

    return (provided_checksum == (osszeg % 11))

print("2. feladat: Adatok beolvasása, tárolása")
f = open('./SzulSzam/vas.txt', 'r')
adatok: List[Szemelyi] = []
for line in f:
    sor = line.strip()
    adatok.append(
        Szemelyi(
            sor[0],
            sor[2:4],
            sor[4:6],
            sor[6:8],
            sor[9:12],
            sor[12],
            sor,
        )
    )

f.close()

print("3. feladat: Ellenőrzés")
szurt_adatok_temp = []
for adat in adatok:
    if CdvEll(adat.raw):
        szurt_adatok_temp.append(adat)
    else:
        print(f"\tHibás a {adat.raw} személyi azonosító!")

adatok = szurt_adatok_temp[:]
del szurt_adatok_temp

print(f"5. feladat: Vas megyében a vizsgált évek alatt {len(adatok)} csecsemő született.")

fiuk_count = 0
for adat in adatok:
    if adat.ferfi:
        fiuk_count += 1
print(f"6.feladat: Fiúk száma: {fiuk_count}")

date_min = adatok[0].szul_ev
date_max = adatok[0].szul_ev
for adat in adatok:
    if adat.szul_ev < date_min:
        date_min = adat.szul_ev
    if adat.szul_ev > date_max:
        date_max = adat.szul_ev
print(f"7. feladat: Vizsgált időszak: {date_min} - {date_max}")

van_szokonapi = False
for adat in adatok:
    if adat.szul_ev % 4 == 0:
        if adat.honap == 2 and adat.nap == 24:
            van_szokonapi = True
            break

if van_szokonapi:
    print("8. feladat: Szökőnapon született baba!")
else:
    print("8. feladat: Nincs szökőnapon született baba!")

print("9. feladat: Statisztika")
ev_stat = {}
for adat in adatok:
    if adat.szul_ev not in ev_stat:
        ev_stat[adat.szul_ev] = 0
    ev_stat[adat.szul_ev] += 1

for ev in ev_stat:
    print(f"\t{ev} - {ev_stat[ev]} fő")
