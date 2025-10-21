#Aumento Salarial

salary = float(input("Qual o valor do salário? "))

if salary > 0 and salary <= 1250.00:
    result = salary * 1.15
    print(f"O salário com o aumento será: {result:.2f}") 
elif salary > 1250.00:
    result = salary * 1.1
    print(f"O salário com o aumento será: {result:.2f}")
else:
    print("Salário inválido")