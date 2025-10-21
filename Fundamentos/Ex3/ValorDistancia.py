#Vamos trabalhar com distâncias exatas

distance = int(input("Qual distância você irá percorrer? "))

if distance > 0 and distance <= 200:
    valor = distance * 0.5
    print(f"O valor final é: {valor:.2f}")
elif distance > 200:
    valor = distance * 0.35
    print(f"O valor final é: {valor:.2f}")
else:
    print("Valor inválido") 
