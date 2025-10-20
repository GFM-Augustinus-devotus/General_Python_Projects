"""**kwargs em Python permite que uma função receba um número variável de argumentos nomeados, ou seja, argumentos no formato chave=valor. 
Dentro da função, esses argumentos são coletados em um dicionário.
 É uma forma de adicionar flexibilidade a uma função, permitindo que ela aceite parâmetros extras sem que a assinatura da função precise ser modificada a cada vez. """

#Chave --> Valor. JSON

games = {
    "name": "Fifa 23",
    "yearLaunch": 2023,
    "gamePrice": 90.50,
    "classification": 8.5,
    "style": ["esporte" , "família"]
}

print(games)
print(len(games))
print(type(games))

#Recuperando valores:

print(games["style"])
print(games.get("classification"))

#Recuperar apenas as chaver ou apenas os valores

print(games.keys())
print(games.values())

#Adicionar itens no dicionario

games["Players"] = 2

print(games)

#Atualizar valores

games.update({"style": ["esporte", "adulto"]})
print(games)


#Remover itens

games.pop("yearLaunch")
print(games)