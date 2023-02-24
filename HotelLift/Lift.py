from typing import List


class LiftData:
    def __init__(self, date, id_card, start_level, end_level):
        self.date = date
        self.id_card = int(id_card)
        self.start_level = int(start_level)
        self.end_level = int(end_level)


adatok: List[LiftData] = []


def feladat1():
    f = open("lift.txt", "r", encoding="utf-8")
    for sor in f:
        split_data = sor.strip().split(' ')
        adatok.append(
            LiftData(
                split_data[0],
                split_data[1],
                split_data[2],
                split_data[3]
            )
        )
    f.close()

def feladat3():
    print(f"3. feladat: Összes lifthasználat: {len(adatok)}")

def feladat4():
    print(f"4. feladat: Időszak: {adatok[0].date} - {adatok[-1].date}")

def feladat5():
    legnagyobb_szint = max(adatok, key=lambda x: x.end_level)
    print(f"5. feladat: Célszint max: {legnagyobb_szint.end_level}")

def feladat6():
    print("6. feladat:")
    id_card_in = 0
    try:
        id_card_in = int(input("\tKártya száma: "))
    except ValueError:
        id_card_in = 5
    
    end_level_in = 0
    try:
        end_level_in = int(input("\tCélszint száma: "))
    except ValueError:
        end_level_in = 5

    return {
        "id_card": id_card_in,
        "end_level": end_level_in
    }

def feladat7(user_input):
    found = False
    for adat in adatok:
        if adat.id_card == user_input["id_card"] and adat.end_level == user_input["end_level"]:
            found = True
            break
    print(f"7. feladat: A(z) {user_input['id_card']}. kártyával{'' if found else ' nem'} utaztak a(z) {user_input['end_level']}. emeletre!")

def feladat8():
    print("8. feladat: Statisztika")
    date_before = adatok[0].date
    counter = 0
    for adat in adatok:
        if adat.date != date_before:
            print(f"\t{adat.date} - {counter}x")
            counter = 0
        counter += 1
        date_before = adat.date

def main():
    feladat1()
    feladat3()
    feladat4()
    feladat5()
    user_input = feladat6()
    feladat7(user_input)
    feladat8()

main()