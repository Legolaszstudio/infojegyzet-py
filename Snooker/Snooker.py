data = []


class snooker_player():
    def __init__(self, helyezes, nev, orszag, nyeremeny):
        self.helyezes = helyezes
        self.nev = nev
        self.orszag = orszag
        self.nyeremeny = nyeremeny


# 2. feladat
def read_data():
    lines = open("snooker.txt", "r", encoding="utf-8").readlines()
    for line in lines[1:]:
        split = line.rstrip("\n").split(";")
        data.append(
            snooker_player(
                int(split[0]),
                split[1],
                split[2],
                int(split[3]),
            )
        )

# 3. feladat
def count_data():
    print(f"3. feladat: A világranglistán {len(data)} versenyző szerepel")

# 4. feladat
def avg_income():
    income_sum = 0
    for player in data:
        income_sum += player.nyeremeny

    osszeg_str = str(round(income_sum/len(data), 2)).replace('.', ',')
    if len(osszeg_str.split(',')[1]) != 2:
        osszeg_str = osszeg_str + '0'

    print(f"4. feladat: A versenyzők átlagosan {osszeg_str} fontot kerestek")


# 5. feladat
def find_wealthiest_player_by_country(fcountry, valtoszam):
    filtered_by_country = list(
        filter(
            lambda x: x.orszag == fcountry,
            data
        )
    )
    wealthiest = 0
    wealthiest_amount = 0
    for player in filtered_by_country:
        if player.nyeremeny > wealthiest_amount:
            wealthiest_amount = player.nyeremeny
            wealthiest = player
    print(f"5. feladat: A legjobban kereső {fcountry}i versenyző:")
    print(f"\tHelyezés: {wealthiest.helyezes}")
    print(f"\tNév: {wealthiest.nev}")
    print(f"\tOrszág: {wealthiest.orszag}")
    nyeremeny_formatted = decimal_format(wealthiest.nyeremeny * valtoszam)
    print(f"\tNyeremény összege: {nyeremeny_formatted} Ft")

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

#6. feladat
def has_country(fcountry):
    country_map = {
        "Norvégia": "norvég",
    }
    country_str = fcountry
    if fcountry in country_map:
        country_str = country_map[fcountry]

    for player in data:
        if player.orszag == fcountry:
            print(f"6. feladat: A versenyzők között van {country_str} versenyző")
            return

    print(f"6. feladat: A versenyzők között nincs {country_str} versenyző")

#7. feladat
def players_by_country():
    print("7. feladat: Statisztika")
    country_count = {}
    for player in data:
        if player.orszag in country_count:
            country_count[player.orszag] += 1
        else:
            country_count[player.orszag] = 1

    for country in country_count:
        if country_count[country] > 4:
            print(f"\t{country} - {country_count[country]} fő")

def main():
    read_data()
    count_data()
    avg_income()
    find_wealthiest_player_by_country("Kína", 380)
    has_country("Norvégia")
    players_by_country()


main()
print()
