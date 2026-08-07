import sys

i = int(sys.argv[1])
a = float(sys.argv[2])
b = float(sys.argv[3])
c = float(sys.argv[4])

lista = [a,b,c]
match i:
    case 1:
        print(sorted(lista))
    case 2:
        print(sorted(lista, reverse=True))
    case 3:
        lista.sort()
        print(f"{lista[0]} - {lista[2]} - {lista[1]}")
