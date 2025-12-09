principal = float(input("Introdu principalul: "))
rate = float(input("Introdu rata anuala a dobanzii: "))
time = float(input("Introdu timpul in ani: "))

interest = (principal * rate * time) / 100

print("Dobanda este: ", interest)