# Primeiros 60 números de Fibonac... qualquercoisa

a, b = 1, 1
print(a)
print(b)

for _ in range(58):
    c = a + b
    print(c)
    a, b = b, c