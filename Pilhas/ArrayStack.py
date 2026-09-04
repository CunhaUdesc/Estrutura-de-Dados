class ArrayStack:
    def __init__(self):
      self.data = []
      self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def push(self, e):
        self.data.append(e)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self.size -= 1
        return self.data.pop(-1)

    def __str__(self):
        # Para imprimir a pilha (print)
        content = '( '
        for element in self.data:
            content += element + ' '
        content += ')'
        return content

    def clear(self):
        while not self.is_empty():
            print(self.pop())
        self.size = 0

    def clear_recursiva(self):
        if not self.is_empty():
            print(self.pop())
            self.clear_recursiva()
            