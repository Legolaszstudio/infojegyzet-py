from typing import List


class Jackie:
    def __init__(self, year, races, wins, podiums, poles, fastests):
        self.year = int(year)
        self.races = int(races)
        self.wins = int(wins)
        self.podiums = int(podiums)
        self.poles = int(poles)
        self.fastests = int(fastests)


adatok: List[Jackie] = []


def feladat2():
    f = open("jackie.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        split = sor.strip().split('\t')
        adatok.append(
            Jackie(
                split[0],
                split[1],
                split[2],
                split[3],
                split[4],
                split[5],
            )
        )


def feladat3():
    print(f"3. feladat: {len(adatok)}")


def feladat4():
    maxos = max(adatok, key=lambda x: x.races)
    print(f"4. feladat: {maxos.year}")


def feladat5():
    stats = {}
    for adat in adatok:
        if str(adat.year)[2] not in stats:
            stats[str(adat.year)[2]] = 0
        stats[str(adat.year)[2]] += adat.wins
    print("5. feladat:")
    for key, value in stats.items():
        print(f"\t{key}0-es évek: {value} megnyert verseny")


def feladat6():
    f = open("jackie.html", "w", encoding="utf-8")

    table = ""
    for adat in adatok:
        table += f"""
            <tr>
                <td>{adat.year}</td>
                <td>{adat.races}</td>
                <td>{adat.wins}</td>
            </tr>
        """

    f.write(f"""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jackie Stewart</title>
    <style>
        td {{
            border: 1px solid black;
        }}
    </style>
</head>
<body>
    <h1>Jackie Stewart</h1>
    <table>
        {
            table
        }
    </table>
</body>
</html>
    """)
    f.close()
    print("6. feladat: jackie.html")


def main():
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()


main()
