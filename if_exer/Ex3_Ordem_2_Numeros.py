num1 = int(input("Numero1: "))
num2 = int(input("Numero2: "))

crescente = sorted([num1, num2])
decrescente = sorted([num1, num2], reverse=True)
print("Crescente:", crescente[0], ",", crescente[1])
print("Decrescente:", decrescente[0], ",", decrescente[1])