num1 = int(input("Numero1: "))
num2 = int(input("Numero2: "))
num3 = int(input("Numero3: "))

nums = [num1, num2, num3]
print("Crescente:", *sorted(nums))
print("Decrescente:", *sorted(nums, reverse=True))