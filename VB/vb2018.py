from typing import List


class Stadion:
    def __init__(self, varos, nev, nev2, ferohely):
        self.varos: str = varos
        self.nev: str = nev
        self.nev2: str = nev2
        self.ferohely = int(ferohely)


adatok: List[Stadion] = []


def feladat1():
    f = open("vb2018.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        adat_split = sor.strip().split(';')
        adatok.append(
            Stadion(
                adat_split[0],
                adat_split[1],
                adat_split[2],
                adat_split[3]
            )
        )
    f.close()

def feladat3():
    print(f"3. feladat: Stadionok száma: {len(adatok)}")

def feladat4():
    legkisebb = adatok[0]
    for adat in adatok:
        if adat.ferohely < legkisebb.ferohely:
            legkisebb = adat
    print(f"4. feladat: A legkevesebb férőhely:")
    print(f"\tVáros: {legkisebb.varos}")
    print(f"\tStadion neve: {legkisebb.nev}")
    print(f"\tFérőhely: {legkisebb.ferohely}")

def feladat5():
    suma = 0
    for adat in adatok:
        suma += adat.ferohely
    avg_string = str(round(suma / len(adatok), 1)).replace('.', ',')
    print(f"5. feladat: Átlagos férőhelyszám: {avg_string}")

def feladat6():
    alternativak = 0
    for adat in adatok:
        if adat.nev2.lower() != 'n.a.':
            alternativak += 1
    print(f"6. feladat: Két néven is ismert stadionok száma: {alternativak}")

def feladat7():
    varos_in = ""
    while len(varos_in) < 3:
        varos_in = input("7. feladat: Kérem a város nevét: ")
    return varos_in

def feladat8(varos):
    found = False
    for adat in adatok:
        if adat.varos.lower() == varos.lower():
            found = True
            break
    
    print(f"8. feladat: A megadott város {'' if found else 'nem '}VB helyszín.")

def feladat9():
    varosok = []
    for adat in adatok:
        if adat.varos not in varosok:
            varosok.append(adat.varos)
    print(f"9. feladat: {len(varosok)} különböző városban voltak mérkőzések.")

def main():
    feladat1()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    varos = feladat7()
    feladat8(varos)
    feladat9()

main()