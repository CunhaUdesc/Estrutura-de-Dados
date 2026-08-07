import sys

print("Salário: ")
salario = float(sys.argv[1])

print("Aumento: ")
aumento = float(sys.argv[2])

print(f"Aumento: {aumento}% - Novo Salário: {salario + (salario * (aumento/100))}")