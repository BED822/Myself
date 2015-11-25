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
            print(str(Two_Dice_Combos.index(i)) +
            "-" + str(Combos_Copies1.index(j)) + 
            " " + str(compare(i,j)))
