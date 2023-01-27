from statistics import mean

class Dolgozo:
    def __init__(self, nev: str, nem: str, reszleg: str, belepes: str, ber: str):
        self.nev = nev
        self.nem = nem
        self.reszleg = reszleg
        self.belepes = int(belepes)
        self.ber = int(ber)

def decimal_format(szam):
    str_szam = str(szam)
    out = ""
    i = 0
    for c in str_szam[::-1]:
        if i == 3:
            out += " "
            i = 0
        out += c
        i += 1
    return out[::-1]

def main():
    # Read data
    adatok = []
    f = open('./Berek/berek2020.txt', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        splitdata = sor.split(';')
        adatok.append(
            Dolgozo(
                splitdata[0],
                splitdata[1],
                splitdata[2],
                splitdata[3],
                splitdata[4]
            )
        )

    # 3. feladat
    print(f'3. feladat: Dolgozók száma: {adatok.__len__()} fő')

    # 4. feladat
    atlag = round(mean([dolgozo.ber for dolgozo in adatok])/1000, 1)
    atlag = str(atlag).replace('.', ',')
    print(f'4. feladat: Bérek átlaga: {atlag} eFt')

    # 5. feladat
    input_reszleg = input('5. feladat: Kérem egy részleg nevét: ')

    # 6. feladat
    reszleg_filtered = list(filter(lambda x: x.reszleg == input_reszleg, adatok))
    if reszleg_filtered.__len__() == 0:
        print(f'6. feladat: A megadott részleg nem létezik a cégnél!')
    else:
        max_dolg = max(reszleg_filtered, key=lambda x: x.ber)
        print(f'6. feladat: A legtöbbet kereső dolgozó a megadott részlegen')
        print(f'\tNév: {max_dolg.nev}')
        print(f'\tNem: {max_dolg.nem}')
        print(f'\tBelépés: {max_dolg.belepes}')
        print(f'\tBér: {decimal_format(max_dolg.ber)} Forint')

    # 7. feladat
    print('7. feladat: Statisztika')
    reszlegek = {}
    for dolgozo in adatok:
        if dolgozo.reszleg not in reszlegek:
            reszlegek[dolgozo.reszleg] = 0
        reszlegek[dolgozo.reszleg] += 1
    for reszleg in reszlegek:
        print(f'\t{reszleg} - {reszlegek[reszleg]} fő')

main()