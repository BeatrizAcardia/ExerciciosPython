mor = (float(input("Digite a quantidade de MORANGOS em quilos: ")))
mac = (float(input("Digite a quantidade de MAÇÃS em quilos: ")))

if(mor <= 5.0):
    mor = 12.50
elif(mor >= 5.0):
    mor = 12.20

if(mac <= 5):
    mac = 9.90
elif(mac >= 5):
    mac = 9.30

total = (mac+mor)

if total > 125.00:
    total *= 0.90

print(total)