import random

colors = ["Brown", "Light Blue", "Pink", "Orange", "Red", "Yellow", "Green", "Dark Blue", "Utilities"]

opponents = 1
turns = 100
games = 500000


def turn(square):
    die_1 = 0
    die_2 = 0
    doubles = 0
    while die_1 == die_2 and doubles < 3:
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        square += (die_1 + die_2)
        if die_1 == die_2:
            doubles += 1
    if doubles >= 3 or square == 30:
        square = 10  # sent to jail
    while square >= 40:
        square -= 40

    # CHANCE

    if square == 7 or square == 22 or square == 36:
        chance = random.randint(0, 15)
        if chance == 0:  # go back three spaces
            square -= 3
        elif chance == 1:  # advance to nearest utility
            if (28 <= chance <= 39) or (0 <= chance <= 11):
                square = 12
            else:
                square = 28
        elif chance == 2:  # advance to Illinois Avenue
            square = 24
        elif chance == 3:  # advance to Go
            square = 0
        elif chance == 4:  # advance to St. Charles Place
            square = 11
        elif chance == 5 or chance == 9:  # advance to nearest Railroad
            if 5 <= square <= 14:
                square = 15
            elif 15 <= square <= 24:
                square = 25
            elif 25 <= square <= 34:
                square = 35
            else:
                square = 5
        elif chance == 6:  # Reading Railroad
            square = 5
        elif chance == 7:  # Go to Jail
            square = 10
        elif chance == 8:  # Advance to Boardwalk
            square = 39

    # COMMUNITY CHEST

    if square == 2 or square == 17 or square == 33:
        cc = random.randint(0, 15)
        if cc == 0:  # Go to Jail
            square = 10
        elif cc == 1:  # Advance to Go
            square = 0

    if square == 30:  # redundancy
        square = 10

    return square

print("Simulating a lot of Monopoly")

squares = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0]

properties = ["GO", "Mediterranean Avenue", "Community Chest 1", "Baltic Avenue", "Income Tax", "Reading Railroad",
              "Oriental Avenue", "Chance 1", "Vermont Avenue", "Connecticut Avenue", "Jail", "St. Charles Place",
              "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad", "St. James Place",
              "Community Chest 2", "Tennessee Avenue", "New York Avenue", "Free Parking", "Kentucky Avenue",
              "Chance 2", "Indiana Avenue", "Illinois Avenue", "B. & O. Railroad", "Atlantic Avenue", "Ventnor Avenue",
              "Water Works", "Marvin Gardens", "GO TO JAIL", "Pacific Avenue", "North Carolina Avenue",
              "Community Chest 3", "Pennsylvania Avenue", "Short Line", "Chance 3", "Park Place", "Luxury Tax",
              "Boardwalk"]


counter1 = 0
counter2 = 0
counter3 = 0

while counter1 < games:
    s = 0
    counter2 = 0
    counter1 += 1
    while counter2 < turns:
        s = turn(s)
        squares[s] += 1
        counter2 += 1
        counter3 += 1


# Basic Percentages
counter1 = 0
for i in range(len(squares)):
    percentage = (float(squares[i] / counter3) * 100)
    print(str(round(percentage, 4)) + '\t' + properties[i])
    counter1 += 1

print("\n\nBasic income")

# Expected income from basic rent
counter1 = 0
for i in range(len(squares)):
    cost = 0
    rent = 0
    percentage = float(squares[i] / counter3)
    # profit = income - cost
    # income = rent * (percentage * number of turns * number of opponents)
    if i == 1:  # Mediterranean
        cost = 60
        rent = 2
    elif i == 3:  # Baltic
        cost = 60
        rent = 4
    elif i == 5:  # Reading R.
        cost = 200
        rent = 25
    elif i == 6:  # Oriental
        cost = 100
        rent = 6
    elif i == 8:  # Vermont
        cost = 100
        rent = 6
    elif i == 9:  # Connecticut
        cost = 120
        rent = 8
    elif i == 11:  # St. Charles
        cost = 140
        rent = 10
    elif i == 12:  # Electric Company
        cost = 150
        rent = 28
    elif i == 13:  # States
        cost = 140
        rent = 10
    elif i == 14:  # Virginia
        cost = 160
        rent = 12
    elif i == 15:  # Pennsylvania R.
        cost = 200
        rent = 25
    elif i == 16:  # St. James
        cost = 180
        rent = 14
    elif i == 18:  # Tennessee
        cost = 180
        rent = 14
    elif i == 19:  # New York
        cost = 200
        rent = 16
    elif i == 21:  # Kentucky
        cost = 220
        rent = 18
    elif i == 23:  # Indiana
        cost = 220
        rent = 18
    elif i == 24:  # Illinois
        cost = 240
        rent = 20
    elif i == 25:  # B. & O. R.
        cost = 200
        rent = 25
    elif i == 26:  # Atlantic
        cost = 260
        rent = 22
    elif i == 27:  # Ventnor
        cost = 260
        rent = 22
    elif i == 28:  # Water Works
        cost = 150
        rent = 28
    elif i == 29:  # Marvin Gardens
        cost = 280
        rent = 24
    elif i == 31:  # Pacific
        cost = 300
        rent = 26
    elif i == 32:  # North Carolina
        cost = 300
        rent = 26
    elif i == 34:  # Pennsylvania Ave.
        cost = 320
        rent = 28
    elif i == 35:  # Short Line
        cost = 200
        rent = 25
    elif i == 37:  # Park Place
        cost = 350
        rent = 35
    elif i == 39:  # Boardwalk
        cost = 400
        rent = 50

    if rent != 0:
        print(str(round(((rent * turns * opponents * percentage) - cost), 4)) + "\t" + str(properties[i]))


# Expected income from one house
print("\n\nOne house")

num_colors = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(squares)):
    cost = 0
    rent = 0
    profit = 0
    percentage = float(squares[i] / counter3)
    # profit = income - cost
    # income = rent * (percentage * number of turns * number of opponents)
    if i == 1:  # Mediterranean
        cost = 110
        rent = 10
    elif i == 3:  # Baltic
        cost = 110
        rent = 20
    elif i == 6:  # Oriental
        cost = 150
        rent = 30
    elif i == 8:  # Vermont
        cost = 150
        rent = 30
    elif i == 9:  # Connecticut
        cost = 170
        rent = 40
    elif i == 11:  # St. Charles
        cost = 240
        rent = 50
    elif i == 13:  # States
        cost = 240
        rent = 50
    elif i == 14:  # Virginia
        cost = 260
        rent = 60
    elif i == 16:  # St. James
        cost = 280
        rent = 70
    elif i == 18:  # Tennessee
        cost = 280
        rent = 70
    elif i == 19:  # New York
        cost = 300
        rent = 80
    elif i == 21:  # Kentucky
        cost = 370
        rent = 90
    elif i == 23:  # Indiana
        cost = 370
        rent = 90
    elif i == 24:  # Illinois
        cost = 390
        rent = 100
    elif i == 26:  # Atlantic
        cost = 410
        rent = 110
    elif i == 27:  # Ventnor
        cost = 410
        rent = 110
    elif i == 29:  # Marvin Gardens
        cost = 430
        rent = 120
    elif i == 31:  # Pacific
        cost = 500
        rent = 130
    elif i == 32:  # North Carolina
        cost = 500
        rent = 130
    elif i == 34:  # Pennsylvania Ave.
        cost = 520
        rent = 150
    elif i == 37:  # Park Place
        cost = 550
        rent = 175
    elif i == 39:  # Boardwalk
        cost = 600
        rent = 200

    if rent != 0:
        profit = round(((rent * turns * opponents * percentage) - cost), 4)
        if i == 1 or i == 3:
            num_colors[0] += profit
        elif i == 6 or i == 8 or i == 9:
            num_colors[1] += profit
        elif i == 11 or i == 13 or i == 14:
            num_colors[2] += profit
        elif i == 16 or i == 18 or i == 19:
            num_colors[3] += profit
        elif i == 21 or i == 23 or i == 24:
            num_colors[4] += profit
        elif i == 26 or i == 27 or i == 29:
            num_colors[5] += profit
        elif i == 31 or i == 32 or i == 34:
            num_colors[6] += profit
        elif i == 37 or i == 39:
            num_colors[7] += profit
        print(str(profit) + "\t" + str(properties[i]))

print()

for i in range(len(colors) - 1):
    print(colors[i] + "\t" + str(round(num_colors[i], 4)))


# Expected income from two houses
print("\n\nTwo houses")

num_colors = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(squares)):
    cost = 0
    rent = 0
    profit = 0
    percentage = float(squares[i] / counter3)
    # profit = income - cost
    # income = rent * (percentage * number of turns * number of opponents)
    if i == 1:  # Mediterranean
        cost = 160
        rent = 30
    elif i == 3:  # Baltic
        cost = 160
        rent = 60
    elif i == 6:  # Oriental
        cost = 200
        rent = 90
    elif i == 8:  # Vermont
        cost = 200
        rent = 90
    elif i == 9:  # Connecticut
        cost = 220
        rent = 100
    elif i == 11:  # St. Charles
        cost = 340
        rent = 150
    elif i == 13:  # States
        cost = 340
        rent = 150
    elif i == 14:  # Virginia
        cost = 360
        rent = 180
    elif i == 16:  # St. James
        cost = 380
        rent = 200
    elif i == 18:  # Tennessee
        cost = 380
        rent = 200
    elif i == 19:  # New York
        cost = 400
        rent = 220
    elif i == 21:  # Kentucky
        cost = 520
        rent = 250
    elif i == 23:  # Indiana
        cost = 520
        rent = 250
    elif i == 24:  # Illinois
        cost = 540
        rent = 300
    elif i == 26:  # Atlantic
        cost = 560
        rent = 330
    elif i == 27:  # Ventnor
        cost = 560
        rent = 330
    elif i == 29:  # Marvin Gardens
        cost = 580
        rent = 360
    elif i == 31:  # Pacific
        cost = 700
        rent = 390
    elif i == 32:  # North Carolina
        cost = 700
        rent = 390
    elif i == 34:  # Pennsylvania Ave.
        cost = 720
        rent = 450
    elif i == 37:  # Park Place
        cost = 750
        rent = 500
    elif i == 39:  # Boardwalk
        cost = 800
        rent = 600

    if rent != 0:
        profit = round(((rent * turns * opponents * percentage) - cost), 4)
        if i == 1 or i == 3:
            num_colors[0] += profit
        elif i == 6 or i == 8 or i == 9:
            num_colors[1] += profit
        elif i == 11 or i == 13 or i == 14:
            num_colors[2] += profit
        elif i == 16 or i == 18 or i == 19:
            num_colors[3] += profit
        elif i == 21 or i == 23 or i == 24:
            num_colors[4] += profit
        elif i == 26 or i == 27 or i == 29:
            num_colors[5] += profit
        elif i == 31 or i == 32 or i == 34:
            num_colors[6] += profit
        elif i == 37 or i == 39:
            num_colors[7] += profit
        print(str(profit) + "\t" + str(properties[i]))

print()

for i in range(len(colors) - 1):
    print(colors[i] + "\t" + str(round(num_colors[i], 4)))


# Expected income from three houses
print("\n\nThree houses")

num_colors = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(squares)):
    cost = 0
    rent = 0
    profit = 0
    percentage = float(squares[i] / counter3)
    # profit = income - cost
    # income = rent * (percentage * number of turns * number of opponents)
    if i == 1:  # Mediterranean
        cost = 210
        rent = 90
    elif i == 3:  # Baltic
        cost = 210
        rent = 180
    elif i == 6:  # Oriental
        cost = 250
        rent = 270
    elif i == 8:  # Vermont
        cost = 250
        rent = 270
    elif i == 9:  # Connecticut
        cost = 270
        rent = 300
    elif i == 11:  # St. Charles
        cost = 440
        rent = 450
    elif i == 13:  # States
        cost = 440
        rent = 450
    elif i == 14:  # Virginia
        cost = 460
        rent = 500
    elif i == 16:  # St. James
        cost = 480
        rent = 550
    elif i == 18:  # Tennessee
        cost = 480
        rent = 550
    elif i == 19:  # New York
        cost = 500
        rent = 600
    elif i == 21:  # Kentucky
        cost = 670
        rent = 700
    elif i == 23:  # Indiana
        cost = 670
        rent = 700
    elif i == 24:  # Illinois
        cost = 690
        rent = 750
    elif i == 26:  # Atlantic
        cost = 710
        rent = 800
    elif i == 27:  # Ventnor
        cost = 710
        rent = 800
    elif i == 29:  # Marvin Gardens
        cost = 730
        rent = 850
    elif i == 31:  # Pacific
        cost = 900
        rent = 900
    elif i == 32:  # North Carolina
        cost = 900
        rent = 900
    elif i == 34:  # Pennsylvania Ave.
        cost = 920
        rent = 1000
    elif i == 37:  # Park Place
        cost = 950
        rent = 1100
    elif i == 39:  # Boardwalk
        cost = 1000
        rent = 1400

    if rent != 0:
        profit = round(((rent * turns * opponents * percentage) - cost), 4)
        if i == 1 or i == 3:
            num_colors[0] += profit
        elif i == 6 or i == 8 or i == 9:
            num_colors[1] += profit
        elif i == 11 or i == 13 or i == 14:
            num_colors[2] += profit
        elif i == 16 or i == 18 or i == 19:
            num_colors[3] += profit
        elif i == 21 or i == 23 or i == 24:
            num_colors[4] += profit
        elif i == 26 or i == 27 or i == 29:
            num_colors[5] += profit
        elif i == 31 or i == 32 or i == 34:
            num_colors[6] += profit
        elif i == 37 or i == 39:
            num_colors[7] += profit
        print(str(profit) + "\t" + str(properties[i]))

print()

for i in range(len(colors) - 1):
    print(colors[i] + "\t" + str(round(num_colors[i], 4)))


# Expected income from four houses
print("\n\nFour houses")

num_colors = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(squares)):
    cost = 0
    rent = 0
    profit = 0
    percentage = float(squares[i] / counter3)
    # profit = income - cost
    # income = rent * (percentage * number of turns * number of opponents)
    if i == 1:  # Mediterranean
        cost = 260
        rent = 160
    elif i == 3:  # Baltic
        cost = 260
        rent = 320
    elif i == 6:  # Oriental
        cost = 300
        rent = 400
    elif i == 8:  # Vermont
        cost = 300
        rent = 400
    elif i == 9:  # Connecticut
        cost = 320
        rent = 450
    elif i == 11:  # St. Charles
        cost = 540
        rent = 625
    elif i == 13:  # States
        cost = 540
        rent = 625
    elif i == 14:  # Virginia
        cost = 560
        rent = 700
    elif i == 16:  # St. James
        cost = 580
        rent = 750
    elif i == 18:  # Tennessee
        cost = 580
        rent = 750
    elif i == 19:  # New York
        cost = 600
        rent = 800
    elif i == 21:  # Kentucky
        cost = 820
        rent = 875
    elif i == 23:  # Indiana
        cost = 820
        rent = 875
    elif i == 24:  # Illinois
        cost = 840
        rent = 925
    elif i == 26:  # Atlantic
        cost = 860
        rent = 975
    elif i == 27:  # Ventnor
        cost = 860
        rent = 975
    elif i == 29:  # Marvin Gardens
        cost = 880
        rent = 1025
    elif i == 31:  # Pacific
        cost = 1100
        rent = 1100
    elif i == 32:  # North Carolina
        cost = 1100
        rent = 1100
    elif i == 34:  # Pennsylvania Ave.
        cost = 1120
        rent = 1200
    elif i == 37:  # Park Place
        cost = 1150
        rent = 1300
    elif i == 39:  # Boardwalk
        cost = 1200
        rent = 1700

    if rent != 0:
        profit = round(((rent * turns * opponents * percentage) - cost), 4)
        if i == 1 or i == 3:
            num_colors[0] += profit
        elif i == 6 or i == 8 or i == 9:
            num_colors[1] += profit
        elif i == 11 or i == 13 or i == 14:
            num_colors[2] += profit
        elif i == 16 or i == 18 or i == 19:
            num_colors[3] += profit
        elif i == 21 or i == 23 or i == 24:
            num_colors[4] += profit
        elif i == 26 or i == 27 or i == 29:
            num_colors[5] += profit
        elif i == 31 or i == 32 or i == 34:
            num_colors[6] += profit
        elif i == 37 or i == 39:
            num_colors[7] += profit
        print(str(profit) + "\t" + str(properties[i]))

print()

for i in range(len(colors) - 1):
    print(colors[i] + "\t" + str(round(num_colors[i], 4)))


# Expected income from hotels
print("\n\nHotel")

num_colors = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(squares)):
    cost = 0
    rent = 0
    profit = 0
    percentage = float(squares[i] / counter3)
    # profit = income - cost
    # income = rent * (percentage * number of turns * number of opponents)
    if i == 1:  # Mediterranean
        cost = 310
        rent = 250
    elif i == 3:  # Baltic
        cost = 310
        rent = 450
    elif i == 6:  # Oriental
        cost = 350
        rent = 550
    elif i == 8:  # Vermont
        cost = 350
        rent = 550
    elif i == 9:  # Connecticut
        cost = 370
        rent = 600
    elif i == 11:  # St. Charles
        cost = 640
        rent = 750
    elif i == 12:  # Electric
        cost = 150
        rent = 70
    elif i == 13:  # States
        cost = 640
        rent = 750
    elif i == 14:  # Virginia
        cost = 660
        rent = 900
    elif i == 16:  # St. James
        cost = 680
        rent = 950
    elif i == 18:  # Tennessee
        cost = 680
        rent = 950
    elif i == 19:  # New York
        cost = 700
        rent = 1000
    elif i == 21:  # Kentucky
        cost = 970
        rent = 1050
    elif i == 23:  # Indiana
        cost = 970
        rent = 1050
    elif i == 24:  # Illinois
        cost = 990
        rent = 1100
    elif i == 26:  # Atlantic
        cost = 1010
        rent = 1150
    elif i == 27:  # Ventnor
        cost = 1010
        rent = 1150
    elif i == 28:  # Water Works
        cost = 150
        rent = 70
    elif i == 29:  # Marvin Gardens
        cost = 1030
        rent = 1200
    elif i == 31:  # Pacific
        cost = 1300
        rent = 1275
    elif i == 32:  # North Carolina
        cost = 1300
        rent = 1275
    elif i == 34:  # Pennsylvania Ave.
        cost = 1320
        rent = 1400
    elif i == 37:  # Park Place
        cost = 1350
        rent = 1500
    elif i == 39:  # Boardwalk
        cost = 1400
        rent = 2000

    if rent != 0:
        profit = round(((rent * turns * opponents * percentage) - cost), 4)
        if i == 1 or i == 3:
            num_colors[0] += profit
        elif i == 6 or i == 8 or i == 9:
            num_colors[1] += profit
        elif i == 11 or i == 13 or i == 14:
            num_colors[2] += profit
        elif i == 16 or i == 18 or i == 19:
            num_colors[3] += profit
        elif i == 21 or i == 23 or i == 24:
            num_colors[4] += profit
        elif i == 26 or i == 27 or i == 29:
            num_colors[5] += profit
        elif i == 31 or i == 32 or i == 34:
            num_colors[6] += profit
        elif i == 37 or i == 39:
            num_colors[7] += profit
        elif i == 12 or i == 28:
            num_colors[8] += profit

        print(str(profit) + "\t" + str(properties[i]))

print()

for i in range(len(colors)):
    print(colors[i] + "\t" + str(round(num_colors[i], 4)))
