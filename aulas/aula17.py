n = [2, 5, 3, 6, 8]
n[2] = 18
print(n)
n.append(55)
n.sort(reverse=True) #tambemreverte[::-1]
print(n)
n.sort()
print(n)
n.insert(1, 29)
print(n)
if 29 in n:
    n.remove(29)
    print('REMOVIDO')
    print(n)
else:
    print('NÃO ACHEI')
    print(n)
values = []
for i in range(1, 6):
    values.append(i)
for chave, value in enumerate(values):
    print(f'In the position {chave+1} I found the value {value}')