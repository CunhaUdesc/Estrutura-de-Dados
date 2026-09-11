from Node import Node

class ListaDupla:

    def __init__(self):
        self.header = Node(None)
        self.trailer = Node(None)
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, valor):
        novo = Node(valor)

        if self.is_empty():
            self.header.next = novo
            self.trailer.left = novo
        else:
            novo.proximo = self.header
            self.header.next = novo

        self.size += 1

    
    def add_last(self, valor):
        novo = Node(valor)

        if self.is_empty():
            self.header.next = novo
            self.trailer.left = novo
        else:
            novo.left = self.trailer.left
            novo.next = self.trailer

        self.trailer.left.next = novo
        self.trailer.left = novo

        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None

        removido = self.header.next

        self.header.next = removido.next
        removido.next.left = self.header

        self.size -= 1

        return removido.valor

    def remove_last(self):
        if self.is_empty():
            return None

        removido = self.trailer.left

        self.trailer.left = removido.left
        removido.left.next = self.trailer

        self.size -= 1

        return removido.valor

    def first(self):
        if self.is_empty():
            return None

        return self.header.next.valor

    def last(self):
        if self.is_empty():
            return None

        return self.trailer.left.valor

    def mostrar(self):
        atual = self.header.next

        while atual != self.trailer:
            print(atual.valor, end=" ")
            atual = atual.next

        print()
    