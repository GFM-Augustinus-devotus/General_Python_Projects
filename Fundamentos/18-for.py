
gamesList = ["GTA V", "Skyrim", "Yu-gi-oh", "NFS", "Fifa", "The Witcher"]

for game in gamesList:
    print(game)
print("-----------")
# Break: interrompe o Loop
for game in gamesList:
    if game == "NFS":
        break
    print(game)
print("-----------")     
# Continue: pula para a próxima iteração
for game in gamesList:
    if game == "NFS":
        continue
    print(game)
print("-----------")

#Avaliação dos games

gameName = input("\nEscolha um jogo: ")

for game in gamesList:
    if gameName == game:
        condition = True
        print(gameName)
        break
    else:
        condition = False
        continue

if condition:
    gameRating = int(input("\nQuantas avaliações você irá fazer? "))

    sum = 0
    for i in range(gameRating):
        nota = float(input("\nDigite a nota para o jogo: "))
        sum += nota

    print(f"\nMédia de avaliação do jogo {gameName} é {sum/gameRating :.2f}")
else:
    print(f"\nO jogo {gameName} não está na lista de jogos!")