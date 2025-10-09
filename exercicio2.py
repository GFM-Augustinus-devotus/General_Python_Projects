# 1º desafio: fifa 23 ---> fi$a 23

gameName = "fifa 23"

gameName = gameName[::-1].replace('f', '$', 1) # inverti a string e substituí apenas o primeiro f

print(gameName[::-1]) # inverti de volta para mostrar o resultado de forma correta

# abc xyz ---> xyc abz 

primeiro = 'abc'

segundo = 'xyz'

print("Resultado: " , segundo.split('z')[0] + primeiro.split('b')[1] , " " , primeiro.split('c')[0] + segundo.split('y')[1])