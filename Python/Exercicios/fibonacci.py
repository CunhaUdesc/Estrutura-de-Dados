
import sys



n = int(sys.argv[1])
def calcula(n):
    if n <= 1:
        return n
    return calcula(n - 1) + calcula(n - 2)

for i in range(n):
    print(calcula(i), end=" ")