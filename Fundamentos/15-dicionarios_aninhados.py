#KWARGS e dicionários podem ser bem poderosos para a estrutura de dados
import pprint

gamesDict = {
    "Resident Evil 4":{
        "Year Launch": 2009,
        "Classification": 9.5,
        "style": ["Ação", "Aventura"]
    },
    "The Elder Scrolls": {
        "Year Launch": 2011,
        "Classification": 10.0,
        "style": ["RPG", "Aventura"]
    },
    "Yu-Gi-Oh Duelist of Roses": {
    "Year Launch": 1996,
    "Classification": 9.7,
    "style": ["Cards", "Terror"]
    }

}
#Melhorando a visulaização do dicionário com a biblioteca nativa do python chamaga pprint
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

#mostrando uma informação específica

print(f"Nota do The Elder Scrolls: {gamesDict["The Elder Scrolls"]["Classification"]}")

#Adicionar item

gamesDict["Yu-Gi-Oh Duelist of Roses"]["Year Launch"] = 1995

print(gamesDict["Yu-Gi-Oh Duelist of Roses"])

#Excluir um dicionário

del gamesDict["Resident Evil 4"]
pp.pprint(gamesDict)