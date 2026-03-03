n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1*2 + n2*3 + n3*5) / 10

print(f"Media: {media:.1f}")
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")