name = input("Nome do jogo:")
yearLaunch = int(input("\nAno de lançamento:"))
grade = float(input("\nNota do jogo:"))

if grade > 8.0 and yearLaunch > 2010:
    print(f"O jogo {name} é um ótimo jogo para ser jogado")
else:
    print(f"O jogo {name} não é um bom jogo para ser jogado")