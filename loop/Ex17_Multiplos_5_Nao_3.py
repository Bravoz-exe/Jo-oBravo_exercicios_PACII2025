
# Multiplos de 5 e não de 3

for i in range(1, 1001):
    if i % 5 == 0 and i % 3 != 0:
        print(i)