nome = input("Nome do cliente: ")
compra = float(input("Valor da compra: "))

if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20
total = compra - desconto
print(f"Nome: {nome}")
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total que tem de pagar: {total:.2f}€")