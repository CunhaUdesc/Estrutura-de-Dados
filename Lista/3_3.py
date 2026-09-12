from ListaDupla import ListaDupla

L = ListaDupla()
M = ListaDupla()

L.add_first(1)
L.add_first(2)
L.add_first(3)
L.add_first(4)
L.add_first(5)
L.add_first(6)
print(L)

M.add_first(1)
M.add_first(2)
M.add_first(3)
M.add_first(4)
M.add_first(5)
M.add_first(6)

def printa(lista):
    atual = lista.header
    while atual is not None:
        print(atual.valor)
        atual = atual.next

print('Lista 1:')
printa(L)
print('\nLista 2:')
printa(M)
print('Nova lista: \n')

def junta_lista(lista1, lista2):
    nova = ListaDupla()

    atual = lista1.header
    while atual is not None:
        nova.add_first(atual.valor)
        atual = atual.next

    atual = lista2.header
    while atual is not None:
        nova.add_first(atual.valor)
        atual = atual.next

    return nova

printa(junta_lista(L, M))
