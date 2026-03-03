segundos = int(input("Digita os segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60
print(f"{horas} hora ou horas, {minutos} minuto ou minutos e {segundos_restantes} segundo ou segundos")