
tipo = input('Informe o tipo de instalação (R, C, I): ')

consumo = float(input('Informe o consumo (kWh): '))

match tipo:
    case 'R':
        if (consumo <= 500):
            preco = 0.4
        else:
            preco = 0.6

    case 'C':
        if (consumo <= 1000):
            preco = 0.55
        else:
            preco = 0.6

    case 'I':
        if (consumo <= 5000):
            preco = 0.57
        else:
            preco = 0.68

print(f'Valor Total: R${consumo * preco:.2f}')