from random import randint

vetor = []
for i in range(0, 50):
    i = randint(0, 20)
    vetor.append(i)
print(vetor)
print('-'*30)
print(f'A soma dos valores é {sum(vetor)}')
print('-' * 30)
print(f'O número de ocorrência de 9 é {vetor.count(9)}')
print('-' * 30)
print(f'O maior valor é {max(vetor)}')
print('-' * 30)
print(f'O menor valor é {min(vetor)}')