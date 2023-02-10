betu_to_morze = {}
morze_to_betu = {}

f = open("./Morze/morzeabc.txt", "r", encoding="utf-8")
f.readline()
for sor in f:
    sor_split = sor.strip().split('\t')
    betu_to_morze[sor_split[0]] = sor_split[1]
    morze_to_betu[sor_split[1]] = sor_split[0]
f.close()

# 3. feladat
print(f"3. feladat: A morze abc {len(betu_to_morze)} db karakter kódját tartalmazza.")

# 4. feladat
betu = input("4. feladat: Kérek egy karaktert: ")
if betu in betu_to_morze:
    print(f"\tA {betu} betű morze kódja: {betu_to_morze[betu]}")
else:
    print("\tNem található a kódtárban ilyen karakter!")

# 5. feladat
def Morze2Szoveg(morse):
    text = ""
    input_split = morse.split(" " * 3)
    for morze_morzsa in input_split:
        if len(morze_morzsa) == 0:
            continue
        if " " in morze_morzsa:
            text += " "
            morze_morzsa = morze_morzsa[1:]
        text += morze_to_betu[morze_morzsa]
    return text

f = open("./Morze/morze.txt", "r", encoding="utf-8")
idezetek = []
for sor in f:
    sor_split = sor.strip().split(';')
    idezetek.append({
        "szerzo": Morze2Szoveg(sor_split[0]),
        "idezet": Morze2Szoveg(sor_split[1])
    })
f.close()

# 7. feladat
print(f"7. feladat: Az első idézet szerzője: {idezetek[0]['szerzo']}")

# 8. feladat
leghoszabb = max(
    idezetek,
    key=lambda idezet: len(idezet["idezet"])
)
print(f"8. feladat: Az leghosszabb idézet szerzője és az idézet: {leghoszabb['szerzo']}: {leghoszabb['idezet']}")

# 9. feladat
print("9. feladat: Arisztotelész idézetei: ")
for idezet in idezetek:
    if idezet["szerzo"].lower() == "arisztotelész":
        print(f"\t- {idezet['idezet']}")

# 10. feladat
f = open("./Morze/forditas.txt", "w", encoding="utf-8")
for idezet in idezetek:
    f.write(f"{idezet['szerzo']}:{idezet['idezet']}\n")
f.close()