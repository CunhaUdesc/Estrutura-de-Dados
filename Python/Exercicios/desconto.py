import sys

preco = float(sys.argv[1])
desconto =  float(sys.argv[2])

print(f"Valor final: {preco - (preco * (desconto/100))}")
