## Utilizando arranjos

class Deque:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.arranjo = [None] * capacidade
        self.inicio = 0
        self.fim = -1
        self.tamanho = 0

    def esta_vazio(self):
        return self.tamanho == 0

    def esta_cheio(self):
        return self.tamanho == self.capacidade

    def inserir_fim(self, valor):
        if self.esta_cheio():
            print("Deque cheio!")
            return

        self.fim = (self.fim + 1) % self.capacidade
        self.arranjo[self.fim] = valor
        self.tamanho += 1

    def inserir_inicio(self, valor):
        if self.esta_cheio():
            print("Deque cheio!")
            return

        self.inicio = (self.inicio - 1) % self.capacidade
        self.arranjo[self.inicio] = valor

        if self.tamanho == 0:
            self.fim = self.inicio

        self.tamanho += 1

    def remover_inicio(self):
        if self.esta_vazio():
            print("Deque vazio!")
            return None

        valor = self.arranjo[self.inicio]
        self.arranjo[self.inicio] = None

        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1

        return valor

    def remover_fim(self):
        if self.esta_vazio():
            print("Deque vazio!")
            return None

        valor = self.arranjo[self.fim]
        self.arranjo[self.fim] = None

        self.fim = (self.fim - 1) % self.capacidade
        self.tamanho -= 1

        return valor

    def primeiro(self):
        if self.esta_vazio():
            return None

        return self.arranjo[self.inicio]

    def mostrar(self):
        if self.esta_vazio():
            print("Deque vazio!")
            return

        atual = self.inicio

        for _ in range(self.tamanho):
            print(self.arranjo[atual], end=" ")
            atual = (atual + 1) % self.capacidade

        print()