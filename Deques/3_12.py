from Deque import Deque

deq = Deque(10)

deq.inserir_inicio(3)
deq.inserir_fim(8)
deq.inserir_fim(9)
deq.inserir_inicio(1)
print(deq.fim)
print(deq.esta_vazio())
deq.inserir_inicio(2)
deq.remover_fim()
deq.inserir_fim(7)
print(deq.inicio)
print(deq.fim)
deq.inserir_fim(4)
print(deq.tamanho)
deq.remover_inicio()
deq.remover_inicio()

[1, 3, 8, 9]
