Red = [4, 4, 4, 4, 4, 9]
Yellow = [3, 3, 3, 3, 8, 8]
Blue = [2, 2, 2, 7, 7, 7]
Magenta = [1, 1, 6, 6, 6, 6]
Olive = [0, 5, 5, 5, 5, 5]

# Blue>Magenta>Olive>Red>Yellow>Blue # Alphabetic order
# Red>Blue>Olive>Yellow>Magenta>Red  # Number of letters

def combo(a, b):
    k = []
    for i in a:
        for j in b:
            k.append(i+j)
    k.sort()
    return k

Blue_Double = combo(Blue, Blue)
Blue_Magenta = combo(Blue, Magenta)
Blue_Olive = combo(Blue, Olive)
Blue_Red = combo(Blue, Red)
Blue_Yellow = combo(Blue, Yellow)
Magenta_Double = combo(Magenta, Magenta)
Magenta_Olive = combo(Magenta, Olive)
Magenta_Red = combo(Magenta, Red)
Magenta_Yellow = combo(Magenta, Yellow)
Olive_Double = combo(Olive, Olive)
Olive_Red = combo(Olive, Red)
Olive_Yellow = combo(Olive, Yellow)
Red_Double = combo(Red, Red)
Red_Yellow = combo(Red, Yellow)
Yellow_Double = combo(Yellow, Yellow)

def compare(a, b, c):
    wins = 0
    ties = 0
    loss = 0
    for i in a:
        for j in b:
            for k in c:
                if i > max(j, k):
                    wins = wins + 1
                elif i == max(j, k):
                    ties = ties + 1
                elif i < max(j, k):
                    loss = loss + 1
    if wins > loss:
        return wins, ties, loss, "<=="
    else:
        return wins, ties, loss, ""

Two_Dice_Combos = [
    Blue_Double, Blue_Magenta, Blue_Olive, 
    Blue_Red, Blue_Yellow, Magenta_Double,
    Magenta_Olive, Magenta_Red, Magenta_Yellow,
    Olive_Double, Olive_Red, Olive_Yellow,
    Red_Double, Red_Yellow, Yellow_Double]
Combos_Copies1 = Two_Dice_Combos
Combos_Copies2 = Two_Dice_Combos

for k in Combos_Copies2:
    for j in Combos_Copies1:
        for i in Two_Dice_Combos:
            wins, ties, loss, arrow = compare(i, j, k)
            if wins > loss:
                print(str(Two_Dice_Combos.index(i)) +
                "-" + str(Combos_Copies1.index(j)) + 
                "-" + str(Combos_Copies1.index(k)) + 
                " " + str(compare(i, j, k)))

"""
4-10-0 (23382, 0, 23274, '<==')
7-10-0 (24048, 0, 22608, '<==')
1-2-2 (23544, 0, 23112, '<==')
12-2-2 (25281, 0, 21375, '<==')
12-5-2 (24756, 0, 21900, '<==')
12-13-2 (24036, 0, 22620, '<==')
13-6-3 (24024, 0, 22632, '<==')
3-9-4 (25308, 0, 21348, '<==')
6-9-4 (23448, 0, 23208, '<==')
14-9-4 (24576, 0, 22080, '<==')
12-2-5 (24756, 0, 21900, '<==')
12-5-5 (24256, 0, 22400, '<==')
12-13-5 (23536, 0, 23120, '<==')
13-3-6 (24024, 0, 22632, '<==')
2-6-6 (24060, 0, 22596, '<==')
5-6-6 (24848, 0, 21808, '<==')
13-6-6 (25856, 0, 20800, '<==')
5-9-6 (23560, 0, 23096, '<==')
13-9-6 (24256, 0, 22400, '<==')
13-14-6 (23840, 0, 22816, '<==')
3-7-7 (23820, 0, 22836, '<==')
3-9-7 (26274, 0, 20382, '<==')
6-9-7 (24580, 0, 22076, '<==')
14-9-7 (25376, 0, 21280, '<==')
3-9-8 (23352, 0, 23304, '<==')
4-10-8 (23880, 0, 22776, '<==')
7-10-8 (24680, 0, 21976, '<==')
3-4-9 (25308, 0, 21348, '<==')
6-4-9 (23448, 0, 23208, '<==')
14-4-9 (24576, 0, 22080, '<==')
5-6-9 (23560, 0, 23096, '<==')
13-6-9 (24256, 0, 22400, '<==')
3-7-9 (26274, 0, 20382, '<==')
6-7-9 (24580, 0, 22076, '<==')
14-7-9 (25376, 0, 21280, '<==')
3-8-9 (23352, 0, 23304, '<==')
3-9-9 (29031, 0, 17625, '<==')
6-9-9 (27616, 0, 19040, '<==')
14-9-9 (27856, 0, 18800, '<==')
3-10-9 (24801, 0, 21855, '<==')
14-10-9 (23920, 0, 22736, '<==')
4-0-10 (23382, 0, 23274, '<==')
7-0-10 (24048, 0, 22608, '<==')
4-8-10 (23880, 0, 22776, '<==')
7-8-10 (24680, 0, 21976, '<==')
3-9-10 (24801, 0, 21855, '<==')
14-9-10 (23920, 0, 22736, '<==')
4-10-10 (25374, 0, 21282, '<==')
7-10-10 (26576, 0, 20080, '<==')
9-10-10 (24275, 0, 22381, '<==')
0-11-11 (23976, 0, 22680, '<==')
8-11-11 (24016, 0, 22640, '<==')
10-11-11 (24136, 0, 22520, '<==')
12-2-13 (24036, 0, 22620, '<==')
12-5-13 (23536, 0, 23120, '<==')
13-6-14 (23840, 0, 22816, '<==')
"""
