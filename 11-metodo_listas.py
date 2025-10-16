gameList = ["NFS", "Resident Evil 4", "Call of Duty", "fifa 25", "Mario Kart"]

print(f"Quantidade de jogos da minha lista: {len(gameList)}")

print(f"Índice Resident Evil 4: {gameList.index("Resident Evil 4")}")

gameList.append("GTA SanAdreas")

print(gameList)

gameList.sort() #Ordenar em ordem alfabética

print(gameList)

#Copiar para uma nova lista algund elementos de um lista existente

gameReset = gameList.copy()
gameReset.remove("Mario Kart")
print(gameReset)

gameList.clear()

if len(gameList) == 0 :
    print("A sua lista de jogos está vazia!")
    print(gameList)
else:
    print("Há jogos na sua lista de jogos")
    print(gameList)