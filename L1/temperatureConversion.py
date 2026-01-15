text_input = input("Introdu temperatura în grade Celsius: ")

text_input_corectat = text_input.replace(',', '.')

try:
    celsius = float(text_input_corectat)

    fahrenheit = celsius * 9 / 5 + 32
    print(f"Temperatura în Fahrenheit este: {fahrenheit}!")

except ValueError:
    print("valoare invalida, trebuie sa fie numar!")