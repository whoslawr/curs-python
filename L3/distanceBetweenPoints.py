import math

def distanta(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

while True:
    try:
        x1 = float(input("Introdu x1: "))
        y1 = float(input("Introdu y1: "))
        x2 = float(input("Introdu x2: "))
        y2 = float(input("Introdu y2: "))

        d = distanta(x1, y1, x2, y2)
        print(f"Distanta dintre puncte este: {d:.2f}")
        break
    except ValueError:
        print("Eroare: Introdu doar numere reale.\n")