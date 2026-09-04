from ArrayStack import ArrayStack

S = ArrayStack()
S.push('A')
S.push('B')
S.push('C')
S.push('D')
print(S)
print(len(S))
print(S.is_empty())
S.push('E')
S.push('F')
print(S.top())
print(S)
print(S.pop())
print(S)

S.clear_recursiva()
print(S)