gameName = "Fifa 23" #São 8 caracteres
gamedescription = """
Fifa 23 é um jogo de futebo desenvolvido pela EA Sports
"""
nome = "oleM satierF leirbaG"
# Toda String a partir da primeira posição. No slice se deixar vazio pega o valor total da posição

print(gameName[0:])


# Toda String a partir da última posição.

print(gameName[:7])

# Pegando apenas uma parte da String do game description

print(gamedescription[1:9])

# Posso indicar o passo ou incremento

print(gamedescription[2:20:2])

# Mostrar todos os caracteres de índice ímpar

print(gamedescription[1::2])

# Palavra de trás para frente

print(gamedescription[::-1])

print(nome[::-1])