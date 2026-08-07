import sys

dias = int(sys.argv[1])
print(f"Dias: {dias}")

horas = int(sys.argv[2])
print(f"Horas: {horas}")

minu = int(sys.argv[3])
print(f"Minutos: {minu}")

seg = int(sys.argv[4])
print(f"Segundos: {seg}")

segundos = dias * 86.400
segundos += horas * 3600
segundos += minu * 60
segundos += seg

print(f"{segundos} segundos")