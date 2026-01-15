def unique_pair_sum(numbers, target):
    perechi = set()
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = numbers[i], numbers[j]
            if a + b == target:
                perechi.add(tuple(sorted((a, b))))
    return perechi

try:
    text_input = input("Introdu numerele separate prin spatiu: ")
    if not text_input.strip():
        raise ValueError("Nu ai introdus numere!")

    numbers_list = [int(x) for x in text_input.split()]

    target_input = input("Introdu valoarea tinta: ")
    if not target_input.strip():
        raise ValueError("Nu ai introdus tinta!")

    target_val = int(target_input)

    rezultat = unique_pair_sum(numbers_list, target_val)
    print("Perechile gasite sunt:")
    print(rezultat)

except ValueError as e:
    print(f"ERROR: {e}")