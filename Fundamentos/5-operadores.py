num1 = int(input("Digite o primeiro numero\n"))
num2 = int(input("Digite o segundo numero\n"))

# Aritmético
sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

mod = num1 % num2
exp = pow(num1, num2)

print(f"Soma: {sum}\nSubtração: {sub}\nMultiplicação: {mult}\nDivisão: {div:.2f}\nResto: {mod}\nPotência: {exp}")

if(num1 > num2):
    print(f"{num1} é maior do que {num2}")
    while(num1 > num2):
        print(f"Num1: {num1} e Num2: {num2}")
        num2 +=1
elif(num1 < num2):
    print(f"{num1} é menor do que {num2}")
    while(num1 > num2):
        print(f"Num1: {num1} e Num2: {num2}")
        num1 +=1
else:
    print(f"{num1} é igual a {num2}")



