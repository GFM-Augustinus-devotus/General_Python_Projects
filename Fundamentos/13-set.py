gameSet = {"NFS", "Resident Evil 4", "Call of Duty", "fifa 25", "Mario Kart"}

print(gameSet)

print(len(gameSet))

# Não é possível recuperar valores via faiamento slice
#True e 1 tem o mesmo valor
#Aceita valores de diferentes tipos

exampleSet = {"PES 2013", True, 1, 90.56}
gameSet.update(exampleSet)
print(gameSet)

#Remover um item do inicioa

gameSet.pop()
print(gameSet)

gameSet.remove("NFS")
print(gameSet)

