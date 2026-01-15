import random

print(" JOC: GHICESTE NUMARUL (1-20) ")
print("Ai exact 5 incercari. Succes!")

numar_secret = random.randint(1, 20)
vieti = 5
castigat = False

while vieti > 0:
    print(f"\nVieti ramase: {vieti}")
    try:
        alegere = int(input("Introdu un numar intre 1 si 20: "))
        if alegere < 1 or alegere > 20:
            print("Eroare: Numarul trebuie sa fie in intervalul [1,20]")
            continue

        if alegere == numar_secret:
            print(f"Ai ghicit numarul {numar_secret}!")
            castigat = True
            break
        elif alegere < numar_secret:
            print("Numar prea mic!")
        else:
            print("Numar prea mare!")

        vieti -= 1

    except ValueError:
        print("ERROR: Introdu un numar valid.")

if not castigat:
    print("\n--- GAME OVER ---")
    print(f"Nu mai ai vieti. Numarul secret era: {numar_secret}")