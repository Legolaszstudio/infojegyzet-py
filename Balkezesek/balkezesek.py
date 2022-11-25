from datetime import datetime
from typing import List


class BaseballPlayer:
    def __init__(self, inp):
        self.name = inp[0]
        self.start_date = datetime.strptime(inp[1], '%Y-%m-%d')
        self.end_date = datetime.strptime(inp[2], '%Y-%m-%d')
        self.weight = int(inp[3])
        self.height = int(inp[4])


adatok: List[BaseballPlayer] = []


def main():
    # 1-2. feladat
    f = open('balkezesek.csv', 'r', encoding='cp1252')
    for line in f.readlines()[1:]:
        adatok.append(BaseballPlayer(line.strip().split(';')))
    f.close()

    # 3. feladat
    print(f"3. feladat: {len(adatok)}")

    # 4. feladat
    print("4. feladat:")
    for player in adatok:
        if player.end_date.year == 1999 and player.end_date.month == 10:
            print(
                f"\t{player.name}, {str(round(player.height*2.54, 1)).replace('.', ',')} cm")

    # 5. feladat
    print("5. feladat:")
    user_input = 0
    while user_input < 1990 or user_input > 1999:
        try:
            user_input = int(input("Kérek egy évszámot 1990 és 1999 között: "))
        except ValueError:
            print("Hibás adat!", end="")
        else:
            if user_input < 1990 or user_input > 1999:
                print("Hibás adat!", end="")

    # 6. feladat
    print("6. feladat:", end="")
    summa = 0
    count = 0
    for player in adatok:
        if player.start_date <= datetime(user_input, 1, 1) <= player.end_date:
            summa += player.weight
            count += 1
    print(f" {str(round(summa/count, 2)).replace('.', ',')} font")


main()
