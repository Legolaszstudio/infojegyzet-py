from typing import List


class Eredmeny:
    def __init__(self, helyezes, versenyzok_szama, sportag, versenyszam):
        self.helyezes = int(helyezes)
        self.versenyzok_szama = int(versenyzok_szama)
        self.sportag: str = sportag
        self.versenyszam: str = versenyszam


adatok: List[Eredmeny] = []
stats = {}


def feladat2():
    f = open("helsinki.txt", "r", encoding="utf-8")
    for line in f:
        sor = line.strip().split(' ')
        adatok.append(
            Eredmeny(
                sor[0],
                sor[1],
                sor[2],
                sor[3]
            )
        )
    f.close()

def feladat3():
    print("3. feladat:")
    print(f"Pontszerző helyezések száma: {len(adatok)}")

def feladat4():
    print("4. feladat:")
    for adat in adatok:
        if adat.helyezes not in stats:
            stats[adat.helyezes] = 0
        stats[adat.helyezes] += 1
    print(f"Arany: {stats[1]}")
    print(f"Ezüst: {stats[2]}")
    print(f"Bronz: {stats[3]}")
    print(f"Összesen: {stats[1] + stats[2] + stats[3]}")

def feladat5():
    print("5. feladat:")
    summa = 0
    for i in range(1, 7):
        summa += stats[i] * (7 - i + (1 if i == 1 else 0))
    print(f"Olimpiai pontok száma: {summa}")

def feladat6():
    print("6. feladat:")
    uszas = sum(
        [1 if adat.helyezes <= 3 and adat.sportag == "uszas" else 0 for adat in adatok]
    )
    torna = sum(
        [1 if adat.helyezes <= 3 and adat.sportag == "torna" else 0 for adat in adatok]
    )
    if uszas > torna:
        print("Úszás sportágban szereztek több érmet.")
    elif torna > uszas:
        print("Torna sportágban szereztek több érmet.")
    else:
        print("Egyenlő volt az érmek száma.")

def feladat7():
    f = open("helsinki2.txt", "w", encoding="utf-8")
    for adat in adatok:
        f.write(
            f"{adat.helyezes} {adat.versenyzok_szama} {(7 - adat.helyezes + (1 if adat.helyezes == 1 else 0))} {adat.sportag.replace('kajakkenu', 'kajak-kenu')} {adat.versenyszam}\n"
        )
    f.close()

def feladat8():
    print("8. feladat:")
    legnagyobb = max(adatok, key=lambda x: x.versenyzok_szama)
    print(f"Helyezés: {legnagyobb.helyezes}")
    print(f"Sportág: {legnagyobb.sportag}")
    print(f"Versenyszám: {legnagyobb.versenyszam}")
    print(f"Sportolók száma: {legnagyobb.versenyzok_szama}")

def main():
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    feladat8()

main()
