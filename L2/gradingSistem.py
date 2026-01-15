try:
    scor = int(input("Introdu scorul: "))
    if scor < 0 or scor > 100:
        print("ERROR: Scorul nu este valid!")
    else:
        note = [
            (90, "Nota A"),
            (80, "Nota B"),
            (70, "Nota C"),
            (60, "Nota D")
        ]
        for prag, nota in note:
            if scor >= prag:
                print(nota)
                break
        else:
            print("Nota F")
except ValueError:
    print("Valoarea introdusa este invalida, introdu un numar din intervalul [0,100]")