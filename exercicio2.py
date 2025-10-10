# 1º desafio: fifa 23 ---> fi$a 23

gameName = "Fifa 23"

gameName = gameName[::-1].replace('f', '$', 1) # inverti a string e substituí apenas o primeiro f

print(gameName[::-1]) # inverti de volta para mostrar o resultado de forma correta

# abc xyz ---> xyc abz 

primeiro = 'abc'

segundo = 'xyz'

print("Resultado: " , segundo.split('z')[0] + primeiro.split('b')[1] , " " , primeiro.split('c')[0] + segundo.split('y')[1])

#----Gabarito 1)

gameName2 = "Fifa 23"
char = gameName2[0].lower()
new_name = gameName2.replace(char, '$')
new_name =  char + new_name[1:]
print(new_name)

#----Gabarito 2)

new_primeiro = segundo[:2] + primeiro[2:]
new_segundo  = primeiro[:2] + segundo[2:]

print(primeiro,  " ---> ", new_primeiro)
print(segundo, " ---> ", new_segundo)

 