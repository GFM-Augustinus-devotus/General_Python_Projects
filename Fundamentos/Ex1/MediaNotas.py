#Cálculo da média de 4 notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

boletim = [nota1, nota2, nota3, nota4]

media = float((nota1 + nota2 + nota3 + nota4) / 4)

print(f"Boletim {boletim}")
print(f"Média: {media:.2f}")