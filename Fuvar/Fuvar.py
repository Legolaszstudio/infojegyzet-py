from typing import List, Literal


class Fuvar:
    def __init__(self, taxi_id, indulas, idotartam, tavolsag, viteldij, borravalo, fizetes_modja) -> None:
        self.taxi_id = int(taxi_id)
        self.indulas: Literal['bankkártya', 'készpénz'] = indulas
        self.idotartam = int(idotartam)
        self.tavolsag = float(tavolsag.replace(',', '.'))
        self.viteldij = float(viteldij.replace(',', '.'))
        self.borravalo = float(borravalo.replace(',', '.'))
        self.fizetes_modja: Literal['bankkártya', 'készpénz'] = fizetes_modja


adatok: List[Fuvar] = []
f = open('fuvar.csv', 'r', encoding='utf-8')
f.readline()
for sor in f:
    sor_split = sor.strip().split(';')
    adatok.append(Fuvar(*sor_split))
f.close()

# 3
print(f'3. feladat: {len(adatok)} fuvar')

# 4
filtered = list(filter(lambda x: x.taxi_id == 6185, adatok))
bevetel = sum(
    map(lambda x: x.viteldij + x.borravalo, filtered), 
)
print(f'4. feladat: {len(filtered)} fuvar alatt: {bevetel}$')

# 5
payment = {}
for fuvar in adatok:
    if fuvar.fizetes_modja in payment:
        payment[fuvar.fizetes_modja] += 1
    else:
        payment[fuvar.fizetes_modja] = 1
print('5. feladat:')
for key, value in payment.items():
    print(f'\t{key}: {value} fuvar')

# 6
milesum = sum(map(lambda x: x.tavolsag, adatok))
print(f'6. feladat: {round(milesum*1.6, 2)}km')

# 7
leghosszabb = max(adatok, key=lambda x: x.idotartam)
print("7. feladat: Leghosszabb fuvar:")
print(f'\tFuvar hossza: {leghosszabb.idotartam} másodperc')
print(f'\tTaxi azonosító: {leghosszabb.taxi_id}')
print(f'\tMegtett távolság: {leghosszabb.tavolsag} km')
print(f'\tViteldíj: {leghosszabb.viteldij}$')

# 8
print('8. feladat: hibak.txt')
hibak = open('hibak.txt', 'w', encoding='utf-8')
hibak.write('taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja\n')
hibasok = []
for fuvar in adatok:
    if fuvar.idotartam > 0 and fuvar.viteldij > 0 and fuvar.tavolsag == 0:
        hibasok.append(fuvar)

hibasok.sort(key=lambda x: x.indulas)
for fuvar in hibasok:
    hibak.write(f'{fuvar.taxi_id};{fuvar.indulas};{fuvar.idotartam};{fuvar.tavolsag};{fuvar.viteldij};{fuvar.borravalo};{fuvar.fizetes_modja}\n')

hibak.close()